from fastapi import APIRouter,Query
from utils.response import response
from utils.dbconnect import mydb
from utils.response import MovieCategoryChoices

router = APIRouter()
mycol = mydb["streamspot"]

@router.post("/add_movies")
def add_movies_api(movie_name,poster_url,movie_link,category: MovieCategoryChoices = Query(
        default=MovieCategoryChoices.ACTION,
        description="Select a country code from the dropdown")):
    try:
        # Create the document to be inserted
        new_movie = {
            "movie_name": movie_name,
            "movie_poster_link": poster_url,
            "movie_link":movie_link,
            "movie_category": category.value,  # Use category value if it's an enum
        }
        
        # Insert the document into the collection
        movie = mycol.insert_one(new_movie)
        
        if movie.inserted_id:
            return response(1004)
        else:
            return response(1008)
        
    except Exception as e:
        return response(1005)