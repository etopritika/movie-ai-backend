# 🎬 Movie AI Backend

This is a lightweight FastAPI backend for movie recommendations powered by a custom ML logic and data from [The Movie Database (TMDb)](https://www.themoviedb.org/).

## 🚀 Features

- 🤖 Get personalized movie recommendations using cosine similarity
- 🧠 Vector-based comparison by genres, rating, and popularity
- 📁 Store and manage a local movie database (`movies.json`)
- 🔄 Weekly movie updates via TMDb API

## 🛠 Tech Stack

- Python 3.10+
- FastAPI
- Uvicorn
- Requests
- Scikit-learn
- NumPy
- Python Dotenv

## 📦 Installation

```bash
git clone https://github.com/your-username/movie-ai-backend.git
cd movie-ai-backend
pip install -r requirements.txt
```

## 🧪 Run the App Locally

```bash
uvicorn main:app --reload
```

Open `http://localhost:8000/docs` to test the API with Swagger UI.

## 🔐 Environment Variables

Create a `.env` file in the root directory:

```
TMDB_API_KEY=your_tmdb_api_key
```

## 🔁 Update Movie Database

### Full Scrape (up to 10,000 top movies)

```bash
python tmdb_scraper.py
```

### Weekly Update (adds only recent releases)

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

Receive top recommended movies based on vector similarity.

## 📐 How It Works

Each movie is converted into a feature vector that includes:
- Genre multi-hot encoding
- Normalized vote average
- Normalized popularity

We use **cosine similarity** to compare your favorites against all movies in the database and return the closest matches.

---

> This project is for learning and experimentation. Not affiliated with TMDb.
