from flask import render_template


def welcome(name):
    context = {
        'name': name
    }
    return render_template('index.html', **context)