from fastapi import APIRouter

from backend.services.service_locator import chat_service

router = APIRouter()


@router.post("/chats")
def create_chat():

    chat = chat_service.create_chat()

    return chat.to_dict()


@router.get("/chats")
def list_chats():

    return chat_service.chat_manager.list_chats()


@router.get("/chats/{chat_id}")
def get_chat(chat_id: str):

    messages = chat_service.chat_manager.get_messages(chat_id)

    return {
        "chat_id": chat_id,
        "messages": messages,
    }