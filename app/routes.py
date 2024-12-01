from app import app
from flask import render_template
from . import views


@app.route('/')
def index():
    return render_template('base.html')

@app.route('/<name>')
def welcome(name):
    return views.welcome(name)