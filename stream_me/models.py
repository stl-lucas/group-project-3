from stream_me import db

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    year = db.Column(db.Integer, unique=False, nullable=False)
    min_age = db.Column(db.Integer, unique=False, nullable=True)
    imdb_score = db.Column(db.Float, unique=False, nullable=True)
    rotten_tomatoes = db.Column(db.Integer, unique=False, nullable=True)
    netflix = db.Column(db.Boolean, default=False)
    hulu = db.Column(db.Boolean, default=False)
    prime = db.Column(db.Boolean, default=False)
    disney = db.Column(db.Boolean, default=False)
    directors = db.Column(db.String(450), unique=False, nullable=True)
    genres = db.Column(db.String(80), unique=False, nullable=True)
    countries = db.Column(db.String(220), unique=False, nullable=True)
    languages = db.Column(db.String(90), unique=False, nullable=True)
    runtime = db.Column(db.Integer, unique=False, nullable=True)

    def __repr__(self):
        return f"Movie('{self.id}', '{self.title}')"

class Shows(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    year = db.Column(db.Integer, unique=False, nullable=False)
    min_age = db.Column(db.Integer, unique=False, nullable=True)
    imdb_score = db.Column(db.Float, unique=False, nullable=True)
    rotten_tomatoes = db.Column(db.Integer, unique=False, nullable=True)
    netflix = db.Column(db.Boolean, default=False)
    hulu = db.Column(db.Boolean, default=False)
    prime = db.Column(db.Boolean, default=False)
    disney = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"TV Show('{self.id}', '{self.title}')"

class Genres(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f"Genre('{self.id}', '{self.description}')"