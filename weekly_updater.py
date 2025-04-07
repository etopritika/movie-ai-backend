# weekly_updater.py
import os
import requests
import json
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"
HEADERS = {"accept": "application/json"}

# 🕒 Обчислюємо діапазон дат: за останній тиждень
today = datetime.today().date()
one_week_ago = today - timedelta(days=7)

# 🔗 Формуємо запит для отримання нових фільмів за останній тиждень без adult-контенту
url = (
    f"{BASE_URL}/discover/movie?api_key={API_KEY}"
    f"&primary_release_date.gte={one_week_ago}"
    f"&primary_release_date.lte={today}"
    f"&include_adult=false"
)

# 📥 Надсилаємо запит
response = requests.get(url, headers=HEADERS)
if response.status_code != 200:
    raise Exception(f"❌ Error {response.status_code}: {response.text}")

data = response.json()
new_movies = []

# 📄 Завантажуємо існуючу базу
with open("movies.json", "r", encoding="utf-8") as f:
    existing_movies = json.load(f)
    existing_ids = {movie["id"] for movie in existing_movies}

# 🔍 Перевіряємо нові фільми
for movie in data.get("results", []):
    if (
        movie.get("vote_average", 0) >= 5 and
        movie.get("popularity", 0) > 5 and
        movie["id"] not in existing_ids
    ):
        new_movies.append(movie)

# ➕ Додаємо нові фільми
updated_movies = existing_movies + new_movies

# 💾 Зберігаємо оновлену базу
with open("movies.json", "w", encoding="utf-8") as f:
    json.dump(updated_movies, f, ensure_ascii=False, indent=2)

print(f"🎉 Weekly update complete. Added {len(new_movies)} new movies.")
