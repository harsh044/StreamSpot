from fastapi import APIRouter
from utils.response import response
from utils.dbconnect import mydb
from bson.json_util import dumps

router = APIRouter()

mycol = mydb["streamspot"]

@router.get("/get_movies")
def get_movies():
    try:
        json_data = [{**i, "_id": str(i["_id"])} for i in mycol.find()]
        if len(json_data)>=1:
            return response(1002,json_data)
        else:
            return response(1008)
        
    except Exception as e:
        return response(1005)