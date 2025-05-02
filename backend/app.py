import os
import random
import requests
from flask import Flask, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

@app.route("/api/movies/random", methods=["GET"])
def get_random_movie():
    # Use TMDb discover or popular endpoint to fetch movies
    page = random.randint(1, 500)  # TMDb allows 500 pages max
    url = f"https://api.themoviedb.org/3/movie/popular?language=en-US&page={page}"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer " + TMDB_API_KEY
    }
    response = requests.get(url, headers=headers)
    data = response.json()

    if "results" in data:
        movie = random.choice(data["results"])
        return jsonify({
            "id": movie["id"],
            "title": movie["title"],
            "poster_path": movie["poster_path"],
            "overview": movie["overview"]
        })


    return jsonify({"error": "Could not fetch movie"}), 500

if __name__ == "__main__":
    app.run(debug=True)
