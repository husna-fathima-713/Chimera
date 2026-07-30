from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from backend.schemas.chat import ChatRequest
from backend.services.chat_service import ChatService

router = APIRouter()

chat_service = ChatService()


@router.post("/chat")
def chat(request: ChatRequest):

    stream = chat_service.chat(
        request.chat_id,
        request.prompt
    )

    return StreamingResponse(
        stream,
        media_type="text/plain"
    )