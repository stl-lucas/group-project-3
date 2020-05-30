from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from stream_me import config

app = Flask(__name__)
app.config['SECRET_KEY'] = config.secret
env = 'dev'

if env == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = config.connection_string
    app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = True
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = config.connection_string
    app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
db = SQLAlchemy(app)


from stream_me import routes