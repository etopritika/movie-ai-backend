from fastapi import FastAPI
from models import MovieRequest
from ml_engine import recommend_movies_by_favorites

app = FastAPI()

@app.post("/recommendations")
def recommend(payload: MovieRequest):
    return recommend_movies_by_favorites(payload.favorites)
