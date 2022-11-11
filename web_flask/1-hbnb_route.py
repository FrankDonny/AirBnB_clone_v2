#!/usr/bin/python3
"""hbnb flask module setup"""
from flask import Flask

app = Flask(__name__)

app.url_map.strict_slashes = False


@app.route('/')
def home():
    """return a string at the root page"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """return a string at the /hbnb page"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)