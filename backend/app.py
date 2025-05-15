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
    # Use TMDb list details endpoint to fetch movies
    page = random.randint(1, 40)  # My list has 40 pages
    url = f"https://api.themoviedb.org/3/list/8529848?language=en-US&page={page}"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer " + TMDB_API_KEY
    }
    response = requests.get(url, headers=headers)
    data = response.json()

    if "items" in data:
        page2 = random.randint(1, 40)  # My list has 40 pages
        url2 = f"https://api.themoviedb.org/3/list/8529848?language=en-US&page={page2}"
        headers2 = {
            "accept": "application/json",
            "Authorization": "Bearer " + TMDB_API_KEY
        }
        response2 = requests.get(url2, headers=headers2)
        data2 = response2.json()
        if "items" in data2:
            movie = random.choice(data["items"])
            movie2 = random.choice(data2["items"])
            if movie2["id"] == movie["id"]:
                page2 = random.randint(1, 40)  # My list has 40 pages
                url2 = f"https://api.themoviedb.org/3/list/8529848?language=en-US&page={page2}"
                response2 = requests.get(url2, headers=headers2)
                data2 = response2.json()
                return jsonify([
                {
                    "id": movie["id"],
                    "title": movie["title"],
                    "poster_path": movie["poster_path"],
                    "overview": movie["overview"],
                    "release_date": movie["release_date"],
                    "vote_average": movie["vote_average"]
                },
                {
                    "id": movie2["id"],
                    "title": movie2["title"],
                    "poster_path": movie2["poster_path"],
                    "overview": movie2["overview"],
                    "release_date": movie2["release_date"],
                    "vote_average": movie2["vote_average"]
                },
                ])
            else:
                return jsonify([
                {
                    "id": movie["id"],
                    "title": movie["title"],
                    "poster_path": movie["poster_path"],
                    "overview": movie["overview"],
                    "release_date": movie["release_date"],
                    "vote_average": movie["vote_average"]
                },
                {
                    "id": movie2["id"],
                    "title": movie2["title"],
                    "poster_path": movie2["poster_path"],
                    "overview": movie2["overview"],
                    "release_date": movie2["release_date"],
                    "vote_average": movie2["vote_average"]
                },
                ])


    return jsonify({"error": "Could not fetch movie"}), 500

if __name__ == "__main__":
    app.run(debug=True)
