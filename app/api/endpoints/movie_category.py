from fastapi import APIRouter,Query
from utils.response import response
from utils.dbconnect import mydb
from utils.response import MovieCategoryChoices

router = APIRouter()
mycol = mydb["streamspot"]    

@router.post("/movie_category")
def movie_category_api(category: MovieCategoryChoices = Query(
        default=MovieCategoryChoices.ACTION,
        description="Select a country code from the dropdown"
    )):
    try:
        json_data = [{**i, "_id": str(i["_id"])} for i in mycol.find({"movie_category": category.value})]
        if json_data:
            return response(1002,json_data)
        else:
            return response(1008)

    except Exception as e:
        return response(1005)