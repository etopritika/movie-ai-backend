# 🎬 Movie AI Backend

This is a lightweight FastAPI backend for movie recommendations powered by a simple ML logic and data from [The Movie Database (TMDb)](https://www.themoviedb.org/).

## 🚀 Features

- 🔥 Get movie recommendations based on your favorite movies
- 📁 Store and manage a local movie database (`movies.json`)
- 🔄 Weekly update of new movies via TMDb API
- 🧠 Simple similarity algorithm based on genre, rating, and popularity

## 🛠 Tech Stack

- Python 3.10+
- FastAPI
- Uvicorn
- Requests
- Python Dotenv

## 📦 Installation

```bash
git clone https://github.com/your-username/movie-ai-backend.git
cd movie-ai-backend
pip install -r requirements.txt
```

## 🧪 Run the app locally

```bash
uvicorn main:app --reload
```

Go to `http://localhost:8000/docs` to try the API with Swagger UI.

## 🔐 Environment Variables

Create a `.env` file in the root of the project:

```
TMDB_API_KEY=your_tmdb_api_key
```

## 🔁 Update movie database

### Full scrape (up to 10,000 top movies):

```bash
python tmdb_scraper.py
```

### Weekly update (add only new movies from last 7 days):

```bash
python weekly_updater.py
```

## 📬 POST /recommendations

Send a list of your favorite movies:

```json
{
  "favorites": [
    {
      "id": 603,
      "title": "The Matrix",
      "genre_ids": [28, 878],
      "vote_average": 8.1,
      "popularity": 45.6,
      "release_date": "1999-03-31"
    }
  ]
}
```

And receive top recommended movies.

---

> This project is for learning and experimentation. Not affiliated with TMDb.
