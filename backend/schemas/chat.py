from pydantic import BaseModel


class ChatRequest(BaseModel):
    chat_id: str
    prompt: str