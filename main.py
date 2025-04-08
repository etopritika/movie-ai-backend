from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from ml_engine import recommend_movies_by_favorites

app = FastAPI()

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

@app.post("/recommendations")
def recommend(payload: MovieRequest):
    return recommend_movies_by_favorites(payload.favorites)
