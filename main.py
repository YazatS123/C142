from flask import Flask, jsonify, request
import csv
all_movies = []

with open('movies.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]

liked_movies = []
disliked_movies = []
not_watched_movies = []

app = Flask(__name__)

@app.route("/get-movie")
def get_movie():
    return jsonify({
        "data": all_movies[0],
        "status": "success"
    })

@app.route("/liked-movie", method=["POST"])
def liked_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    liked_movies.append(movie)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/disliked-movie", method=["POST"])
def disliked_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    disliked_movies.append(movie)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/not-watched-movie", method=["POST"])
def not_watched_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    not_watched_movies.append(movie)
    return jsonify({
        "status": "success"
    }), 201

