from flask import render_template, url_for, flash, redirect, request
from stream_me import app, db
from stream_me.models import Movies, Shows, Genres

@app.route("/")
def home():
    return render_template("index.html")