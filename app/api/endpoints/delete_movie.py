from fastapi import APIRouter
from utils.response import response
from utils.dbconnect import mydb
from bson.objectid import ObjectId

router = APIRouter()
mycol = mydb["streamspot"]

@router.delete("/delete_movie")
def delete_movie_api(movie_id:str):
    try:
        json_data = mycol.delete_one({"_id": ObjectId(movie_id)})
        if json_data:
            return response(1013)
        else:
            return response(1008)

    except Exception as e:
        return response(1005)