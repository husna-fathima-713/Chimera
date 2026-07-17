from fastapi import APIRouter

from backend.services.chat_service import ChatService

router = APIRouter()

chat_service = ChatService()


@router.post("/chats")
def create_chat():

    chat = chat_service.create_chat()

    return chat.to_dict()