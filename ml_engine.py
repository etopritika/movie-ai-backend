import json
from typing import List
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MultiLabelBinarizer, MinMaxScaler
import numpy as np
from models import Movie

with open("movies.json", "r", encoding="utf-8") as f:
    all_movies = json.load(f)

def recommend_movies_by_favorites(favorites: List[Movie], top_n: int = 100):
    favorites_dicts = [
        fav.model_dump() if not isinstance(fav, dict) else fav
        for fav in favorites
    ]

    if not favorites_dicts:
        return {"recommended_movies": []}

    mlb = MultiLabelBinarizer()
    genres_all = [movie.get("genre_ids", []) for movie in all_movies]
    genre_matrix = mlb.fit_transform(genres_all)

    ratings = np.array([movie.get("vote_average", 0) for movie in all_movies]).reshape(-1, 1)
    popularity = np.array([movie.get("popularity", 0) for movie in all_movies]).reshape(-1, 1)

    scaler = MinMaxScaler()
    rating_scaled = scaler.fit_transform(ratings)
    popularity_scaled = scaler.fit_transform(popularity)

    features = np.hstack((genre_matrix, rating_scaled, popularity_scaled))

    favorite_ids = {fav["id"] for fav in favorites_dicts}
    favorite_indices = [
        idx for idx, movie in enumerate(all_movies) if movie["id"] in favorite_ids
    ]
    if not favorite_indices:
        return {"recommended_movies": []}

    favorite_vectors = features[favorite_indices]
    user_profile_vector = np.mean(favorite_vectors, axis=0).reshape(1, -1)

    similarity_scores = cosine_similarity(user_profile_vector, features)[0]

    scored_movies = [
        (score, movie)
        for score, movie in zip(similarity_scores, all_movies)
        if movie["id"] not in favorite_ids
    ]

    scored_movies.sort(key=lambda x: x[0], reverse=True)
    recommended = [movie for _, movie in scored_movies[:top_n]]

    return {
        "recommended_movies": [
            {
                "id": movie["id"],
                "title": movie["title"],
                "genre_ids": movie["genre_ids"],
                "vote_average": movie["vote_average"],
                "popularity": movie["popularity"],
                "release_date": movie["release_date"],
                "poster_path": movie.get("poster_path"),
                "overview": movie.get("overview")
            }
            for movie in recommended
        ]
    }
