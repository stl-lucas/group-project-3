from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
env = 'prod'

if env == 'dev':
    from stream_me import config
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = config.connection_string
    app.config['SECRET_KEY'] = config.secret
    app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = True
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['HEROKU_POSTGRESQL_SILVER_URL']
    app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
    app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
db = SQLAlchemy(app)


from stream_me import routes