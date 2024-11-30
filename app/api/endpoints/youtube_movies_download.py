from fastapi import APIRouter
from utils.response import response
from utils.dbconnect import mydb

router = APIRouter()

mycol = mydb["streamspot"]

@router.get("/download_movies")
def download_movies_api():
    try:
        pass
        
    except Exception as e:
        return response(1005)