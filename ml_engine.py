import json
from typing import List
from collections import Counter

# Завантажуємо всі фільми з JSON
with open("movies.json", "r", encoding="utf-8") as f:
    all_movies = json.load(f)

def recommend_movies_by_favorites(favorites: List[object], top_n: int = 100):
    # Приводимо Pydantic-моделі до dict
    favorites_dicts = [f.dict() if not isinstance(f, dict) else f for f in favorites]

    # Створюємо зведену картину вподобань
    genre_counter = Counter()
    total_rating = 0
    total_popularity = 0

    for movie in favorites_dicts:
        genre_counter.update(movie.get("genre_ids", []))
        total_rating += movie.get("vote_average", 0)
        total_popularity += movie.get("popularity", 0)

    avg_rating = total_rating / len(favorites_dicts) if favorites_dicts else 0
    avg_popularity = total_popularity / len(favorites_dicts) if favorites_dicts else 0
    top_genres = {genre for genre, _ in genre_counter.most_common(5)}

    scored_movies = []

    for movie in all_movies:
        if movie["id"] in [f["id"] for f in favorites_dicts]:
            continue  # Не рекомендуємо ті, що вже є

        movie_genres = set(movie.get("genre_ids", []))
        genre_match = len(movie_genres & top_genres)

        rating_diff = abs(movie.get("vote_average", 0) - avg_rating)
        popularity_diff = abs(movie.get("popularity", 0) - avg_popularity)

        # Чим ближче до 0 — тим краще, тому використовуємо від'ємне значення
        score = genre_match * 2 - rating_diff - (popularity_diff / 100)

        if genre_match > 0:
            scored_movies.append((score, movie))

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
                "poster_path": movie.get("poster_path")
            }
            for movie in recommended
        ]
    }
