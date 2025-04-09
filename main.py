from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import MovieRequest
from ml_engine import recommend_movies_by_favorites

app = FastAPI()

origins = [
    "https://movie-radar-rho.vercel.app",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/recommendations")
def recommend(payload: MovieRequest):
    return recommend_movies_by_favorites(payload.favorites)
