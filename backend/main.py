from fastapi import FastAPI

from backend.api.routes.chat import router as chat_router
from backend.api.routes.chats import router as chats_router
from backend.api.routes.documents import router as documents_router
from backend.api.routes.health import router as health_router

app = FastAPI(title="Chimera")

app.include_router(health_router)
app.include_router(chat_router)
app.include_router(chats_router)
app.include_router(documents_router)