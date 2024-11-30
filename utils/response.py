from fastapi.responses import JSONResponse
from utils.messages import messages
from fastapi import status
from enum import Enum


def response(status_code, data=[]):
    content = messages.get(status_code)
    return JSONResponse(
        {
            "success": content[2],
            "code": status_code,
            "msg": content[0],
            "data": data,
        },
        content[1] or status.HTTP_200_OK,
    )

class MovieCategoryChoices(str, Enum):
    ACTION = "Action"
    COMEDY = "Comedy"
    DRAMA = "Drama"
    HORROR = "Horror"
    ROMANCE = "Romance"
    SCIFI = "Sci-Fi"
    THRILLER = "Thriller"