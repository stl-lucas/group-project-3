from flask import render_template, url_for, flash, redirect, request, jsonify
from stream_me import app, db
from stream_me.models import Services, Movies, Shows, Genres, Countries, Languages, Users
from stream_me.prediction import prediction
from stream_me.feildArray import ensureFieldsAreArrays
from stream_me.codeUtility import generateCode
import json, requests
import pickle

@app.route("/")
def home():
    # Needs new landing page template
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    services = Services.query.all()
    return render_template("dashboard.html", services=services)

@app.route("/analyze", methods=['GET', 'POST'])
def analyze():
    services = Services.query.all()
    if request.method == 'POST':
        email = request.form['email']
        code = request.form['code']
        user = Users.query.filter_by(code=code).first()
        if user:
            if user.email == email:
                state_data = pickle.loads(user.state_data)
                result = Services.query.filter_by(name=prediction(state_data)).first()
                flash(f'Congratulations, your prediciton results are ready!', 'success')
                return redirect(f'analyze?code={user.code}')
            else:
                flash(f'Sorry, your email and code did not match! Please try again.', 'danger')
                return render_template("analyze.html")
        else:
            flash(f'Sorry, your previous prediction was not found! Please try again.', 'danger')
            return render_template("analyze.html")
    else:
        if 'code' in request.args:
            code = request.args['code']
            user = Users.query.filter_by(code=code).first()
            state_data = pickle.loads(user.state_data)
            result = Services.query.filter_by(name=prediction(state_data)).first()
            return render_template("analyze.html", services=services, result=result)
        else:
            return render_template("analyze.html", services=services)

@app.route("/interview", methods=['GET', 'POST'])
def interview():
    if request.method == 'POST':
        email = request.form['InputEmail']
        code = generateCode(5)

        genres, languages, countries, favorites = ensureFieldsAreArrays()

        state_data = {
            'genres': genres,
            'children': request.form['moviesandtvshowschildren'],
            'language': languages,
            'countries': countries,
            'types': request.form['moviesandtvshowstypes'],
            'favorites': favorites,
            'birthday': request.form['moviesandtvshowsbirthday'],
            'pay': request.form['moviesandtvshowspay']
        }
        user = Users(email=email, code=code, state_data=pickle.dumps(state_data))
        
        if Users.query.filter_by(email=email).first():
            flash(f'User email already exists.', 'danger')
            return redirect('interview')
        else:
            db.session.add(user)
            db.session.commit()
            user = Users.query.filter_by(email=email).first()
            flash(f'Congratulations, your prediciton results are ready!', 'success')
            return render_template('user.html', user=user)
    else:
        return render_template("interview.html")


@app.route("/user")
def user():
    return render_template("user.html")

@app.route("/api")
def api():
    return render_template("api.html")

@app.route("/api/v1/services")
def services():
    services = []
    services_list = Services.query.order_by(Services.id).all()
    for service in services_list:
        services.append({
            'id': service.id,
            'name': service.name,
            'price': service.price,
            'url': service.url,
            'logo': f'https://stream-ly.herokuapp.com/static/img/{service.logo}'
        })
    return jsonify(services)

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