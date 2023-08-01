#!/usr/bin/env python3
"""
4-app.py module
"""

from flask import Flask, render_template, request
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


@app.route('/')
def index():
    """
    Basic flask app that renders a html file
    """
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    """
    Determines the best match with the supported languages
    """
    locale_request = request.args.get('locale')
    if locale_request in app.config['LANGUAGES']:
        return locale_request

    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run()
