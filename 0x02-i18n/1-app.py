#!/usr/bin/env python3
"""
1-app.py module
"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """
    Config class that has a LANGUAGES class attribute
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


babel = Babel(app)


@app.route('/')
def index():
    """
    Basic flask app that renders a html file
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
