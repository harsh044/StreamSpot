from fastapi import APIRouter
from utils.response import response
from utils.dbconnect import mydb

router = APIRouter()
mycol = mydb["streamspot"]    

@router.get("/search_movies")
def search_movies_api(keyword):
    try:
        json_data = [{**i, "_id": str(i["_id"])} for i in mycol.find({"movie_name": { "$regex": keyword, "$options": "i" }})]
        if json_data:
            return response(1002,json_data)
        else:
            return response(1008)

    except Exception as e:
        return response(1005)