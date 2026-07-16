from fastapi import APIRouter
from pydantic import BaseModel

from backend.services.chat_service import ChatService
from backend.services.chat_manager import ChatManager

router = APIRouter()

chat_service = ChatService()
chat_manager = ChatManager()


class ChatRequest(BaseModel):
    chat_id: str
    prompt: str


class CreateChatRequest(BaseModel):
    title: str


@router.post("/chat")
def chat(request: ChatRequest):
    response = chat_service.chat(
        request.chat_id,
        request.prompt
    )

    return {
        "response": response
    }


@router.post("/chats")
def create_chat(request: CreateChatRequest):
    chat = chat_manager.create_chat(request.title)
    return chat.to_dict()


@router.get("/chats")
def list_chats():
    return chat_manager.list_chats()