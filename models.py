from pydantic import BaseModel
from typing import List, Optional

class Movie(BaseModel):
    id: int
    title: str
    genre_ids: List[int]
    vote_average: float
    popularity: float
    release_date: str
    poster_path: Optional[str] = None
    overview: Optional[str] = None

class MovieRequest(BaseModel):
    favorites: List[Movie]
