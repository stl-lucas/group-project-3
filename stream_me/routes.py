from flask import render_template, url_for, flash, redirect, request, jsonify
from stream_me import app, db
from stream_me.models import Movies, Shows, Genres, Countries, Languages

@app.route("/")
def home():
    # Needs new landing page template
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/analyze")
def analyze():
    # Needs to return generic visualizations/analysis
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
        return redirect(url_for('prediction?code={{ user.code }}'))
    else:
        return render_template("interview.html")

@app.route("/prediction")
def prediction():
    if 'code' in request.args:
        code = request.args['code']
        #user = Users.query.filter_by(code=code).first()
        return render_template("prediction.html")
    else:
        flash(f'Uh-oh. No user has been found! Please try again.', 'danger')
        return render_template("prediction.html")

@app.route("/api/v1/movies")
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

@app.route("/api/v1/shows")
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

@app.route("/api/v1/genres")
def genres():
    genres = []
    genre_list = Genres.query.all()
    for genre in genre_list:
        genres.append({'id': genre.id, 'description': genre.description})
    return jsonify(genres)

@app.route("/api/v1/countries")
def countries():
    countries = []
    country_list = Countries.query.all()
    for country in country_list:
        countries.append({'id': country.id, 'name': country.name})
    return jsonify(countries)

@app.route("/api/v1/languages")
def languages():
    languages = []
    language_list = Languages.query.all()
    for language in language_list:
        languages.append({'id': language.id, 'description': language.description})
    return jsonify(languages)