from fastapi import FastAPI

from backend.config import APP_NAME, VERSION
from backend.api.routes.health import router as health_router
from backend.api.routes.chat import router as chat_router

app = FastAPI(
    title=APP_NAME,
    version=VERSION,
)

# Register API routers
app.include_router(health_router)
app.include_router(chat_router)


@app.get("/")
def root():
    return {
        "name": APP_NAME,
        "status": "online",
        "version": VERSION,
    }