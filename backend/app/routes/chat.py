from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse, JSONResponse
import json

from app.services import chat as chat_service

router = APIRouter()

@router.get('/approve')
async def approve_research(action: bool, request: Request, thread_id: str):
    
    # service returns either 'error', error_message or 'success', stream_generator
    result, return_object = await chat_service.approve_research(request.app.state.graph, thread_id, action)

    if result == "error":
        return JSONResponse(content=return_object, status_code=400)

    return StreamingResponse(
        return_object(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        },
    )


@router.get('/')
async def chat(prompt: str, request: Request, thread_id: str = None):

    stream_generator = await chat_service.chat(request.app.state.graph, thread_id, prompt)

    return StreamingResponse(
        stream_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        },
    )
