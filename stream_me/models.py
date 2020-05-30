from stream_me import db

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), unique=True, nullable=False)

    def __repr__(self):
        return f"Movie('{self.id}', '{self.title}')"