from fastapi import APIRouter
from utils.response import response
from utils.dbconnect import mydb
from bson.objectid import ObjectId

router = APIRouter()
mycol = mydb["streamspot"]

@router.post("/single_movie")
def single_movie_api(movie_id):
    try:
        json_data = [{**i, "_id": str(i["_id"])} for i in mycol.find({"_id": ObjectId(movie_id)})]
        if json_data:
            return response(1002,json_data[0])
        else:
            return response(1008)

    except Exception as e:
        return response(1005)