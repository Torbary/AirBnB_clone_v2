#!/usr/bin/python3
"""a script that starts a Flask web application"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Route handler for the root endpoint."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route handler for the /hbnb endpoint."""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_text(text):
    """Route handler for the /c/<text> endpoint."""
    # Replace underscore with a space
    text = text.replace('_', ' ')
    return f'C {text}'


if __name__ == '__main__':
    # Run the Flask application on 0.0.0.0:5000
    app.run(host='0.0.0.0', port=5000)
