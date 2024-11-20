from fastapi import APIRouter
from utils.response import response
from utils.dbconnect import mydb

router = APIRouter()
mycol = mydb["users"]

@router.post("/authentication")
def authentication_api(username,password):
    try:
        if mycol.find_one({"username": username, "password": password}):
            return response(1001)
        else:
            return response(1000)
    except Exception as e:
        return response(1005)