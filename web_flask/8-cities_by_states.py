#!/usr/bin/python3
"""hbnb flask module setup"""
from models import storage
from models.city import City
from flask import Flask, render_template
from os import getenv

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def cities_by_states():
    """state list to be returned"""
    if getenv("HBNB_TYPE_STORAGE") == "db":
    cities = storage.all(City)
    sorted_cities = sorted(cities.values(), key=lambda state: cities.name)
    return render_template('7-states_list.html', state=sorted_cities)


@app.teardown_appcontext
def remove_session():
    """closes the current session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
