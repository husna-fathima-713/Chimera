from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {
        "name": "Chimera",
        "status": "online",
        "version": "0.1.0"
    }