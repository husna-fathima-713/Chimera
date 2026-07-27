from fastapi import APIRouter, HTTPException

from backend.services.chat_service import ChatService

router = APIRouter()

chat_service = ChatService()


@router.get("/chats")
def list_chats():
    return chat_service.chat_manager.list_chats()


@router.get("/chats/{chat_id}")
def get_chat(chat_id: str):

    chat = chat_service.chat_manager.load_chat(chat_id)

    if chat is None:
        raise HTTPException(status_code=404, detail="Chat not found")

    return chat


@router.post("/chats")
def create_chat():

    chat = chat_service.create_chat()

    return chat.to_dict()