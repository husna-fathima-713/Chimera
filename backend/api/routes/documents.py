from fastapi import APIRouter, UploadFile, File

from backend.services.chat_service import ChatService

router = APIRouter()

chat_service = ChatService()


@router.post("/documents")

async def upload_document(file: UploadFile = File(...)):

    filepath = f"backend/storage/{file.filename}"

    with open(filepath, "wb") as f:
        f.write(await file.read())

    chat_service.index_document(filepath)

    return {
        "message": "Document indexed successfully."
    }