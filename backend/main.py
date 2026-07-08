from fastapi import FastAPI

from backend.config import APP_NAME, VERSION


app = FastAPI(
    title=APP_NAME,
    version=VERSION,
)


@app.get("/")
def root():
    return {
        "name": APP_NAME,
        "status": "online",
        "version": VERSION,
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }