from pathlib import Path
from fastapi import FastAPI, APIRouter
from app.api.api import api_router

BASE_PATH = Path(__file__).resolve().parent
root_router = APIRouter()
app = FastAPI(title="Test REST API. V1")

app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    # Use this for debugging purposes only       
    uvicorn.run(app, host="0.0.0.0", port=8000)
    # uvicorn.main()