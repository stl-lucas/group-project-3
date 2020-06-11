from stream_me.models import Movies, Shows, Services

# PREDICTION TOOL
def prediction(state_data):

    # define service rating dictionaries
    raw_services = Services.query.all()
    services = []
    for service in raw_services:
        services.append({
            'service': service.name,
            'movies': 0,
            'languages': 0,
            'countries': 0,
            'shows': 0,
            'imdb': 0,
            'imdb_count': 0,
            'tomatoes': 0,
            'tomatoes_count': 0,
            'favs': 0,
            'year': 0,
            'price': 20 - service.price
        })

    # Get all Movies and Shows
    movies = Movies.query.all()
    shows = Shows.query.all()

    # Filter titles by Favorite Genres
    def genre(movie):
        if movie.genres:
            return bool(set(movie.genres.split(",")) & set(state_data['genres']))
        else:
            return False

    filtered_movies = []

    if state_data['children']:
        state_data['genres'].append("Family")

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
            if movie.title in state_data['favorites']:
                services[0]['favs'] += 1
            if movie.languages:
                if bool(set(movie.languages.split(",")) & set(state_data['language'])):
                    services[0]['languages'] += 1
            if movie.countries:
                if bool(set(movie.countries.split(",")) & set(state_data['countries'])):
                    services[0]['countries'] += 1
            if movie.year > state_data['birthday']:
                services[0]['year'] += 1
        if movie.hulu:
            services[1]['movies'] += 1
            if movie.imdb_score:
                services[1]['imdb'] += movie.imdb_score
                services[1]['imdb_count'] += 1
            if movie.rotten_tomatoes:
                services[1]['tomatoes'] += movie.rotten_tomatoes
                services[1]['tomatoes_count'] += 1
            if movie.title in state_data['favorites']:
                services[1]['favs'] += 1
            if movie.languages:
                if bool(set(movie.languages.split(",")) & set(state_data['language'])):
                    services[1]['languages'] += 1
            if movie.countries:
                if bool(set(movie.countries.split(",")) & set(state_data['countries'])):
                    services[1]['countries'] += 1
            if movie.year > state_data['birthday']:
                services[1]['year'] += 1
        if movie.prime:
            services[2]['movies'] += 1
            if movie.imdb_score:
                services[2]['imdb'] += movie.imdb_score
                services[2]['imdb_count'] += 1
            if movie.rotten_tomatoes:
                services[2]['tomatoes'] += movie.rotten_tomatoes
                services[2]['tomatoes_count'] += 1
            if movie.title in state_data['favorites']:
                services[2]['favs'] += 1
            if movie.languages:
                if bool(set(movie.languages.split(",")) & set(state_data['language'])):
                    services[2]['languages'] += 1
            if movie.countries:
                if bool(set(movie.countries.split(",")) & set(state_data['countries'])):
                    services[2]['countries'] += 1
            if movie.year > state_data['birthday']:
                services[2]['year'] += 1
        if movie.disney:
            services[3]['movies'] += 1
            if movie.imdb_score:
                services[3]['imdb'] += movie.imdb_score
                services[3]['imdb_count'] += 1
            if movie.rotten_tomatoes:
                services[3]['tomatoes'] += movie.rotten_tomatoes
                services[3]['tomatoes_count'] += 1
            if movie.title in state_data['favorites']:
                services[3]['favs'] += 1
            if movie.languages:
                if bool(set(movie.languages.split(",")) & set(state_data['language'])):
                    services[3]['languages'] += 1
            if movie.countries:
                if bool(set(movie.countries.split(",")) & set(state_data['countries'])):
                    services[3]['countries'] += 1
            if movie.year > state_data['birthday']:
                services[3]['year'] += 1

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
            if show.title in state_data['favorites']:
                services[0]['favs'] += 1
            if show.year > state_data['birthday']:
                services[0]['year'] += 1
        if show.hulu:
            services[1]['shows'] += 1
            if show.imdb_score:
                services[1]['imdb'] += show.imdb_score
                services[1]['imdb_count'] += 1
            if show.rotten_tomatoes:
                services[1]['tomatoes'] += show.rotten_tomatoes
                services[1]['tomatoes_count'] += 1
            if show.title in state_data['favorites']:
                services[1]['favs'] += 1
            if show.year > state_data['birthday']:
                services[1]['year'] += 1
        if show.prime:
            services[2]['shows'] += 1
            if show.imdb_score:
                services[2]['imdb'] += show.imdb_score
                services[2]['imdb_count'] += 1
            if show.rotten_tomatoes:
                services[2]['tomatoes'] += show.rotten_tomatoes
                services[2]['tomatoes_count'] += 1
            if show.title in state_data['favorites']:
                services[2]['favs'] += 1
            if show.year > state_data['birthday']:
                services[2]['year'] += 1
        if show.disney:
            services[3]['shows'] += 1
            if show.imdb_score:
                services[3]['imdb'] += show.imdb_score
                services[3]['imdb_count'] += 1
            if show.rotten_tomatoes:
                services[3]['tomatoes'] += show.rotten_tomatoes
                services[3]['tomatoes_count'] += 1
            if show.title in state_data['favorites']:
                services[3]['favs'] += 1
            if show.year > state_data['birthday']:
                services[3]['year'] += 1

    # Averaging ratings
    for service in services:
        service['imdb'] = round(service['imdb'] / service['imdb_count'], 2)
        service['tomatoes'] = round(service['tomatoes'] / service['tomatoes_count'], 2)

    # Max category values for normalizing data
    max_movie = max(service['movies'] for service in services)
    max_show = max(service['shows'] for service in services)
    max_lang = max(service['languages'] for service in services)
    max_country = max(service['countries'] for service in services)
    max_imdb = max(service['imdb'] for service in services)
    max_tomato = max(service['tomatoes'] for service in services)
    max_favs = max(service['favs'] for service in services)
    max_year = max(service['year'] for service in services)
    max_price = max(service['price'] for service in services)

    # Metric Weights (key to formulating our proprietary algorithm)
    if state_data['types'] == "Movies":
        movie_weight = 0.75
        show_weight = 0.25
    elif state_data['types'] == "Shows":
        movie_weight = 0
        show_weight = 1
    else:
        movie_weight = 0.5
        show_weight = 0.5
    language_weight = 0.5
    country_weight = 0.5
    imdb_weight = 0.5
    tomato_weight = 0.5
    favs_weight = 3
    year_weight = 2
    price_weight = 2

    # Normalize service metrics for rating
    normalized_services = services
    for service in normalized_services:
        service.pop('imdb_count')
        service.pop('tomatoes_count')
        service['movies'] = round(service['movies'] * 10 / max_movie, 2)
        service['shows'] = round(service['shows'] * 10 / max_show, 2)
        service['languages'] = round(service['languages'] * 10 / max_lang, 2)
        service['countries'] = round(service['countries'] * 10 / max_country, 2)
        service['imdb'] = round(service['imdb'] * 10 / max_imdb, 2)
        service['tomatoes'] = round(service['tomatoes'] * 10 / max_tomato, 2)
        service['year'] = round(service['year'] * 10 / max_year, 2)
        try:
            service['favs'] = round(service['favs'] * 10 / max_favs, 2) 
        except:
            service['favs'] = 0
        service['price'] = round(service['price'] * 10 / max_price, 2)

    # Service rating calculation
    for service in normalized_services:
        service['rating'] = round(service['movies'] * movie_weight + 
                                service['shows'] * show_weight + 
                                service['languages'] * language_weight + 
                                service['countries'] * country_weight + 
                                service['imdb'] * imdb_weight + 
                                service['tomatoes'] * tomato_weight + 
                                service['favs'] * favs_weight +
                                service['year'] * year_weight +
                                service['price'] * price_weight, 2)

    # find max service rating
    prediction_result = max(normalized_services, key=lambda x:x['rating'])

    return prediction_result['service']