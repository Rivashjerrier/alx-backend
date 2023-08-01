#!/usr/bin/env python3
"""
5-app.py module
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    Config class that has a LANGUAGES class attribute
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.route('/')
def index():
    """
    Basic flask app that renders a html file
    """
    return render_template('5-index.html')


@babel.localeselector
def get_locale():
    """
    Determines the best match with the supported languages
    """
    locale_request = request.args.get('locale')
    if locale_request in app.config['LANGUAGES']:
        return locale_request

    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user(user_id):
    """
    returns a user dictionary or None if the ID cannot be found or
    if login_as was not passed
    """
    return users.get(user_id)


@app.before_request
def before_request():
    """
    before_requestuses get_user to find a user if any
    and sets it as a global on flask.g.user
    """
    login_as = request.args.get('login_as')
    if login_as is not None:
        user_id = int(login_as)
        g.user = get_user(user_id)
    else:
        g.user = None


if __name__ == '__main__':
    app.run()
