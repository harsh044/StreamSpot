from fastapi import APIRouter,Query
from utils.response import response
from utils.dbconnect import mydb
from utils.response import MovieCategoryChoices
from bson.objectid import ObjectId

router = APIRouter()
mycol = mydb["streamspot"]

@router.put("/upload_poster")
def upload_poster_api(movie_id,poster_url,category: MovieCategoryChoices = Query(
        default=MovieCategoryChoices.ACTION,
        description="Select a country code from the dropdown")):
    try:
        # Update query where no document matches
        filter = {"_id": ObjectId(movie_id)}
        update = {"$set":{"movie_poster_link": poster_url,"movie_category":category.value}}
        movie = mycol.update_one(filter,update)
        
        if movie.matched_count == 1:
            return response(1006)
        else:
            return response(1008)
        
    except Exception as e:
        return response(1005)