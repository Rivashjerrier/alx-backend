#!/usr/bin/env python3
""" 0-app.py module """

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def main():
    """ Basic flask app that renders a html file """
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
