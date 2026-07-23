from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.routes.health import router as health_router
from backend.api.routes.chat import router as chat_router
from backend.api.routes.chats import router as chats_router
from backend.api.routes.documents import router as documents_router

app = FastAPI(title="Chimera")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(chat_router)
app.include_router(chats_router)
app.include_router(documents_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to Chimera API"
    }