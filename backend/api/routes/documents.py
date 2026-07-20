from fastapi import APIRouter, UploadFile, File
from pathlib import Path
import shutil

from backend.services.chat_service import ChatService

router = APIRouter()

chat_service = ChatService()

DOCUMENTS_DIR = Path("backend/storage/documents")
DOCUMENTS_DIR.mkdir(parents=True, exist_ok=True)


@router.post("/documents")
def upload_document(file: UploadFile = File(...)):

    file_path = DOCUMENTS_DIR / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    chat_service.index_document(str(file_path))

    return {
        "message": "Document indexed successfully",
        "filename": file.filename
    }