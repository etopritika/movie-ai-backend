import os
import requests
import time
import json
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"
HEADERS = {"accept": "application/json"}

all_movies = []

for page in range(1, 501):
    url = (
        f"{BASE_URL}/discover/movie?api_key={API_KEY}"
        f"&sort_by=popularity.desc&page={page}"
        f"&language=en-US&include_adult=false"
    )

    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        print(f"❌ Error {response.status_code} on page {page}")
        break

    data = response.json()
    new_movies = []

    for movie in data.get("results", []):
        release_year = 0
        try:
            release_year = int(movie.get("release_date", "")[:4])
        except ValueError:
            continue

        vote_average = movie.get("vote_average", 0)
        popularity = movie.get("popularity", 0)

        if release_year >= 2000:
            if vote_average >= 5:
                new_movies.append(movie)
        else:
            if vote_average >= 7 and popularity > 15:
                new_movies.append(movie)

    existing_ids = {m["id"] for m in all_movies}
    unique_new_movies = [m for m in new_movies if m["id"] not in existing_ids]

    all_movies.extend(unique_new_movies)

    print(f"✅ {len(all_movies)} p.{page}: added {len(unique_new_movies)} new movies")
    time.sleep(0.3)

with open("movies.json", "w", encoding="utf-8") as f:
    json.dump(all_movies, f, ensure_ascii=False, indent=2)

print(f"🎉 Done. Total movies saved: {len(all_movies)}")
