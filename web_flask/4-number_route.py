#!/usr/bin/env python3
"""
A Flask web application.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route handler for the root endpoint.
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route handler for the /hbnb endpoint.
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_text_c(text):
    """
    Route handler for the /c/<text> endpoint.
    """
    # Replace underscore with a space
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_text_python(text):
    """
    Route handler for the /python/<text> endpoint.
    """
    # Replace underscore with a space
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """
    Route handler for the /number/<n> endpoint.
    """
    return '{} is a number'.format(n)


if __name__ == '__main__':
    # Run the Flask application on 0.0.0.0:5000
    app.run(host='0.0.0.0', port=5000)
