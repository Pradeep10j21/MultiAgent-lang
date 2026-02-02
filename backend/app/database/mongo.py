from app.core.config import settings
from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from mongomock_motor import AsyncMongoMockClient

# Global MongoDB client
mongo_client = None
mongo_db = None

def get_mongo_db() -> AsyncIOMotorDatabase:
    global mongo_db
    if mongo_db is None:
        client = AsyncIOMotorClient(settings.MONGODB_URI, serverSelectionTimeoutMS=2000)
        mongo_db = client[settings.MONGODB_DB_NAME]
    return mongo_db

async def close_mongo_connection():
    global mongo_client, mongo_db
    if mongo_client:
        if hasattr(mongo_client, 'close'):
            mongo_client.close()
        mongo_client = None
        mongo_db = None
