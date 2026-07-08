from fastapi import FastAPI

from backend.api.routes.health import router as health_router
from backend.config import APP_NAME, VERSION

app = FastAPI(
    title=APP_NAME,
    version=VERSION,
)

app.include_router(health_router)


@app.get("/")
def root():
    return {
        "name": APP_NAME,
        "status": "online",
        "version": VERSION,
    }