from flask import request

def ensureFieldsAreArrays():
    genreField = request.form['moviesandtvshowsgenre']
    languageField = request.form['moviesandtvshowslanguage']
    countryField = request.form['moviesandtvshowscountries']
    favoritesField = request.form['moviesandtvshowsfavorites']

    # Genres - make sure it's an array.
    if isinstance(genreField,list):
        genres = genreField
    else:
        genres = [genreField]

    # Languages - make sure it's an array.
    if isinstance(languageField,list):
        languages = languageField
    else:
        languages = [languageField]

    # Countries - make sure it's an array.
    if isinstance(countryField,list):
        countries = countryField
    else:
        countries = [countryField]

    # Favorites - make sure it's an array.
    if isinstance(favoritesField,list):
        favorites = favoritesField
    else:
        favorites = [favoritesField]
    return genres, languages, countries, favorites