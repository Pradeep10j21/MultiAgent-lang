from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver
from langgraph.graph.state import CompiledStateGraph

from app.database.postgres import engine, Base
from app.core.config import settings
from app.routes import chat_router
from app.investment_assistant.graphs import build_research_graph
from app.database.mongo import get_mongo_db, mongo_db
import app.database.mongo as mongo_mod


from langgraph.checkpoint.memory import MemorySaver
import logging
import traceback
from fastapi.responses import JSONResponse

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    checkpointer_manager = None
    checkpointer = None
    
    try:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        print("Postgres initiated")
        
        checkpointer_manager = AsyncPostgresSaver.from_conn_string(settings.DB_URI_CHECKPOINTER)
        checkpointer = await checkpointer_manager.__aenter__()
        await checkpointer.setup()
        print("Postgres Checkpointer initialized")
    except Exception as e:
        print(f"Postgres connection failed: {e}")
        print("Falling back to MemorySaver for checkpointer")
        checkpointer = MemorySaver()

    # Init MongoDB
    try:
        db = get_mongo_db()
        # Ping with a short timeout
        from motor.motor_asyncio import AsyncIOMotorClient
        temp_client = AsyncIOMotorClient(settings.MONGODB_URI, serverSelectionTimeoutMS=2000)
        await temp_client.admin.command('ping')
        print("MongoDB connected")
    except Exception as e:
        print(f"MongoDB connection failed: {e}. Falling back to AsyncMongoMockClient")
        from mongomock_motor import AsyncMongoMockClient
        mock_client = AsyncMongoMockClient()
        mongo_mod.mongo_db = mock_client[settings.MONGODB_DB_NAME]

    app.state.graph = build_research_graph(checkpointer)
    print("Graph initialized")

    yield
    
    if checkpointer_manager:
        await checkpointer_manager.__aexit__(None, None, None)
        print("Postgres connection closed")


app = FastAPI(
    title='Investment Assistant',
    lifespan=lifespan
)

app.include_router(chat_router, prefix='/chat')

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(f"\n--- Incoming Request: {request.method} {request.url} ---")
    try:
        response = await call_next(request)
        print(f"--- Response: {response.status_code} ---")
        return response
    except Exception as e:
        print(f"!!! CRITICAL ERROR in Middleware: {e}")
        traceback.print_exc()
        return JSONResponse(
            status_code=500,
            content={"detail": "Internal Server Error", "error": str(e)},
            headers={
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "*",
                "Access-Control-Allow-Headers": "*",
            }
        )

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    print(f"!!! GLOBAL EXCEPTION: {exc}")
    traceback.print_exc()
    return JSONResponse(
        status_code=500,
        content={"detail": "Global Internal Server Error", "error": str(exc)},
        headers={"Access-Control-Allow-Origin": "*"}
    )

@app.get('/test')
async def test(request: Request):
    graph: CompiledStateGraph = request.app.state.graph
    thread = {"configurable": {"thread_id": '22113'}}

    return await graph.aget_state(config=thread)
