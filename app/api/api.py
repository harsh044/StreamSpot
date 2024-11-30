from fastapi import APIRouter
from app.api.endpoints import home,sync_movies, upload_poster,get_movies,authentication,single_movie,movie_category,search_movie,delete_movie,add_movies,youtube_movies_download

api_router = APIRouter()

api_router.include_router(home.router, prefix="/home", tags=["home"])
api_router.include_router(authentication.router, prefix="/authentication_api", tags=["authentication_api"])
api_router.include_router(sync_movies.router, prefix="/movies_api", tags=["movies_api"])
api_router.include_router(get_movies.router, prefix="/get_movies_api", tags=["get_movies_api"])
api_router.include_router(upload_poster.router, prefix="/upload_poster_api", tags=["upload_poster_api"])
api_router.include_router(single_movie.router, prefix="/single_movie_api", tags=["single_movie_api"])
api_router.include_router(movie_category.router, prefix="/movie_category_api", tags=["movie_category_api"])
api_router.include_router(search_movie.router, prefix="/search_movie_api", tags=["search_movie_api"])
api_router.include_router(delete_movie.router, prefix="/delete_movie_api", tags=["delete_movie_api"])
api_router.include_router(add_movies.router, prefix="/add_movies_api", tags=["add_movies_api"])
api_router.include_router(youtube_movies_download.router, prefix="/youtube_movies_download_api", tags=["youtube_movies_download_api"])