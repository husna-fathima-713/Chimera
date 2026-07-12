from fastapi import APIRouter
from pydantic import BaseModel

from backend.services.chat_service import ChatService

router = APIRouter()

chat_service = ChatService()


class ChatRequest(BaseModel):
    prompt: str


@router.post("/chat")
def chat(request: ChatRequest):
    response = chat_service.chat(request.prompt)

    return {
        "response": response
    }