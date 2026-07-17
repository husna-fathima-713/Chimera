from fastapi import APIRouter
from pydantic import BaseModel

from backend.services.chat_service import ChatService

router = APIRouter()

chat_service = ChatService()


class ChatRequest(BaseModel):
    chat_id: str
    prompt: str


@router.post("/chat")
def chat(request: ChatRequest):
    response = chat_service.chat(
        request.chat_id,
        request.prompt
    )

    return {
        "response": response
    }