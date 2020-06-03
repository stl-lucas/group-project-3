from flask import render_template, url_for, flash, redirect, request, jsonify
from stream_me import app, db
from stream_me.models import Movies, Shows, Genres, Countries, Languages

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/interview")
def interview():
    return render_template("interview.html")

@app.route("/movies")
def movies():
    movies = []
    movie_list = Movies.query.all()
    for movie in movie_list:
        movies.append({
            'id': movie.id,
            'title': movie.title,
            'year': movie.year,
            'min_age': movie.min_age,
            'imdb_score': movie.imdb_score,
            'rotten_tomatoes': movie.rotten_tomatoes,
            'netflix': movie.netflix,
            'hulu': movie.hulu,
            'prime': movie.prime,
            'disney': movie.disney,
            'directors': movie.directors,
            'genres': movie.genres,
            'countries': movie.countries,
            'languages': movie.languages,
            'runtime': movie.runtime
        })
    return jsonify(movies)

@app.route("/shows")
def shows():
    shows = []
    show_list = Shows.query.all()
    for show in show_list:
        shows.append({
            'id': show.id,
            'title': show.title,
            'year': show.year,
            'min_age': show.min_age,
            'imdb_score': show.imdb_score,
            'rotten_tomatoes': show.rotten_tomatoes,
            'netflix': show.netflix,
            'hulu': show.hulu,
            'prime': show.prime,
            'disney': show.disney
        })
    return jsonify(shows)

@app.route("/genres")
def genres():
    genres = []
    genre_list = Genres.query.all()
    for genre in genre_list:
        genres.append({'id': genre.id, 'description': genre.description})
    return jsonify(genres)

@app.route("/countries")
def countries():
    countries = []
    country_list = Countries.query.all()
    for country in country_list:
        countries.append({'id': country.id, 'name': country.name})
    return jsonify(countries)

@app.route("/languages")
def languages():
    languages = []
    language_list = Languages.query.all()
    for language in language_list:
        languages.append({'id': language.id, 'description': language.description})
    return jsonify(languages)