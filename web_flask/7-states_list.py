from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    """state list to be returned"""
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda state: state.name)
    return render_template('7-states_list.html', st=sorted_states)


@app.teardown_appcontext
def remove_session():
    """closes the current session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
