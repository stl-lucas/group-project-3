from flask import render_template, url_for, flash, redirect, request, jsonify
from stream_me import app, db
from stream_me.models import Movies, Shows, Genres, Countries, Languages
import json, requests

@app.route("/")
def home():
    # Needs new landing page template
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/analyze", methods=['GET', 'POST'])
def analyze():
    if request.method == 'POST':
        # Needs to return user specific visualizations/analysis
        # email = request.form['email']
        # code = request.form['code']
        # user = Users.query.filter_by(email=email).filter_by(code=code).first()
        result = prediction()
        return render_template("analyze.html", result=result)
    else:
        # Needs to return generic visualizations/analysis
        if 'code' in request.args:
            code = request.args['code']
            #user = Users.query.filter_by(code=code).first()
            #call prediction function
            return render_template("analyze.html", result=result)
        else:
            return render_template("analyze.html")

@app.route("/api")
def api():
    return render_template("api.html")

@app.route("/interview", methods=['GET', 'POST'])
def interview():
    if request.method == 'POST':
        # email = request.form['email']
        # code = '123456789' # Random Code
        # user_data = {
        #     'genres': request.form['genres'],
        #     'children': request.form['children'],
        #     'ages': request.form['ages'],
        #     'language': request.form['language'],
        #     'countries': request.form['countries'],
        #     'types': request.form['types'],
        #     'favorites': request.form['favorites'],
        #     'birthdate': request.form['birthdate']
        # }
        # user = Users(email=email, code=code, interview=user_data)
        # if Users.query.filter_by(email=email).first():
        #     flash(f'User email already exists.', 'danger')
        #     return redirect(url_for('interview'))
        # else:
        #     db.session.add(user)
        #     db.session.commit()
        #     user = Users.query.filter_by(email=email).first()
        #     flash(f'Congratulations, your prediciton results are ready!', 'success')
        return redirect(url_for('analyze?code={{ user.code }}'))
    else:
        return render_template("interview.html")

@app.route("/api/v1/movies")
def movies():
    movies = []
    movie_list = Movies.query.order_by(Movies.id).all()
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

@app.route("/api/v1/shows")
def shows():
    shows = []
    show_list = Shows.query.order_by(Shows.id).all()
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

@app.route("/api/v1/titles")
def titles():
    titles = []
    movie_list = Movies.query.all()
    show_list = Shows.query.all()
    for movie in movie_list:
        titles.append({'title': movie.title})
    for show in show_list:
        titles.append({'title': show.title})
    return jsonify(titles)

@app.route("/api/v1/genres")
def genres():
    genres = []
    genre_list = Genres.query.order_by(Genres.description).all()
    for genre in genre_list:
        genres.append({'id': genre.id, 'description': genre.description})
    return jsonify(genres)

@app.route("/api/v1/countries")
def countries():
    countries = []
    country_list = Countries.query.order_by(Countries.name).all()
    for country in country_list:
        countries.append({'id': country.id, 'name': country.name})
    return jsonify(countries)

@app.route("/api/v1/languages")
def languages():
    languages = []
    language_list = Languages.query.order_by(Languages.description).all()
    for language in language_list:
        languages.append({'id': language.id, 'description': language.description})
    return jsonify(languages)

# PREDICTION TOOL
def prediction():
    # define user data
    user_data = {
            'genres': ["Adventure" , "Comedy", "Sci-Fi"],
            'children': True,
            'ages': ["G", "PG", "PG-13", "R"],
            'language': ["English"],
            'countries': ["United States"],
            'types': ["Movies"],
            'favorites': ["Back to the Future", "Star Wars: The Empire Strikes Back", "Stranger Things"],
            'birthdate': 1987
        }

    # define service rating dictionaries
    services = [
        {'service': 'netflix', 'movies': 0, 'shows': 0, 'imdb': 0, 'imdb_count': 0, 'tomatoes': 0, 'tomatoes_count': 0, 'favs': 0},
        {'service': 'hulu', 'movies': 0, 'shows': 0, 'imdb': 0, 'imdb_count': 0, 'tomatoes': 0, 'tomatoes_count': 0, 'favs': 0},
        {'service': 'prime', 'movies': 0, 'shows': 0, 'imdb': 0, 'imdb_count': 0, 'tomatoes': 0, 'tomatoes_count': 0, 'favs': 0},
        {'service': 'disney', 'movies': 0, 'shows': 0, 'imdb': 0, 'imdb_count': 0, 'tomatoes': 0, 'tomatoes_count': 0, 'favs': 0},
    ]

    # Get all Movies and Shows
    movies = Movies.query.all()
    shows = Shows.query.all()

    # Filter titles by Favorite Genres
    def genre(movie):
        if movie.genres:
            if bool(set(movie.genres.split(",")) & set(user_data['genres'])):
                return True
            else:
                return False
        else:
            return False

    filtered_movies = []

    for movie in movies:
        if genre(movie):
            filtered_movies.append(movie)

    # Capture Scores on Filtered Movies
    for movie in filtered_movies:
        if movie.netflix:
            services[0]['movies'] += 1
            if movie.imdb_score:
                services[0]['imdb'] += movie.imdb_score
                services[0]['imdb_count'] += 1
            if movie.rotten_tomatoes:
                services[0]['tomatoes'] += movie.rotten_tomatoes
                services[0]['tomatoes_count'] += 1
            if movie.title in user_data['favorites']:
                services[0]['favs'] += 1
        if movie.hulu:
            services[1]['movies'] += 1
            if movie.imdb_score:
                services[1]['imdb'] += movie.imdb_score
                services[1]['imdb_count'] += 1
            if movie.rotten_tomatoes:
                services[1]['tomatoes'] += movie.rotten_tomatoes
                services[1]['tomatoes_count'] += 1
            if movie.title in user_data['favorites']:
                services[1]['favs'] += 1
        if movie.prime:
            services[2]['movies'] += 1
            if movie.imdb_score:
                services[2]['imdb'] += movie.imdb_score
                services[2]['imdb_count'] += 1
            if movie.rotten_tomatoes:
                services[2]['tomatoes'] += movie.rotten_tomatoes
                services[2]['tomatoes_count'] += 1
            if movie.title in user_data['favorites']:
                services[2]['favs'] += 1
        if movie.disney:
            services[3]['movies'] += 1
            if movie.imdb_score:
                services[3]['imdb'] += movie.imdb_score
                services[3]['imdb_count'] += 1
            if movie.rotten_tomatoes:
                services[3]['tomatoes'] += movie.rotten_tomatoes
                services[3]['tomatoes_count'] += 1
            if movie.title in user_data['favorites']:
                services[3]['favs'] += 1

    # Capturing scores on filtered shows
    for show in shows:
        if show.netflix:
            services[0]['shows'] += 1
            if show.imdb_score:
                services[0]['imdb'] += show.imdb_score
                services[0]['imdb_count'] += 1
            if show.rotten_tomatoes:
                services[0]['tomatoes'] += show.rotten_tomatoes
                services[0]['tomatoes_count'] += 1
            if show.title in user_data['favorites']:
                services[0]['favs'] += 1
        if show.hulu:
            services[1]['shows'] += 1
            if show.imdb_score:
                services[1]['imdb'] += show.imdb_score
                services[1]['imdb_count'] += 1
            if show.rotten_tomatoes:
                services[1]['tomatoes'] += show.rotten_tomatoes
                services[1]['tomatoes_count'] += 1
            if show.title in user_data['favorites']:
                services[1]['favs'] += 1
        if show.prime:
            services[2]['shows'] += 1
            if show.imdb_score:
                services[2]['imdb'] += show.imdb_score
                services[2]['imdb_count'] += 1
            if show.rotten_tomatoes:
                services[2]['tomatoes'] += show.rotten_tomatoes
                services[2]['tomatoes_count'] += 1
            if show.title in user_data['favorites']:
                services[2]['favs'] += 1
        if show.disney:
            services[3]['shows'] += 1
            if show.imdb_score:
                services[3]['imdb'] += show.imdb_score
                services[3]['imdb_count'] += 1
            if show.rotten_tomatoes:
                services[3]['tomatoes'] += show.rotten_tomatoes
                services[3]['tomatoes_count'] += 1
            if show.title in user_data['favorites']:
                services[3]['favs'] += 1

    # Averaging ratings
    for service in services:
        service['imdb'] = round(service['imdb'] / service['imdb_count'], 2)
        service['tomatoes'] = round(service['tomatoes'] / service['tomatoes_count'], 2)

    # Max category values for normalizing data
    max_movie = max(service['movies'] for service in services)
    max_show = max(service['shows'] for service in services)
    max_imdb = max(service['imdb'] for service in services)
    max_tomato = max(service['tomatoes'] for service in services)
    max_favs = max(service['favs'] for service in services)

    # Normalize service metrics for rating
    normalized_services = services
    for service in normalized_services:
        service.pop('imdb_count')
        service.pop('tomatoes_count')
        service['movies'] = round(service['movies'] * 10 / max_movie, 2)
        service['shows'] = round(service['shows'] * 10 / max_show, 2)
        service['imdb'] = round(service['imdb'] * 10 / max_imdb, 2)
        service['tomatoes'] = round(service['tomatoes'] * 10 / max_tomato, 2)
        try:
            service['favs'] = round(service['favs'] * 10 / max_favs, 2) 
        except:
            service['favs'] = 0

    # Metric Weights (key to formulating our proprietary algorithm)
    movie_weight = 0.5
    show_weight = 0.5
    imdb_weight = 1.5
    tomato_weight = 1.5
    favs_weight = 4

    # Service rating calculation
    for service in normalized_services:
        service['rating'] = round(service['movies'] * movie_weight + 
                                service['shows'] * show_weight + 
                                service['imdb'] * imdb_weight + 
                                service['tomatoes'] * tomato_weight + 
                                service['favs'] * favs_weight, 2)

    # find max service rating
    prediction_result = max(normalized_services, key=lambda x:x['rating'])

    return prediction_result['service']