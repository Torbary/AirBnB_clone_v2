#!/usr/bin/python3
"""/number_odd_or_even/<n>: display a HTML page only if n is an integer:

    H1 tag: “Number: n is even|odd” inside the tag BODY
"""

from flask import Flask, render_template

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
def display_text_c(text):
    """Route handler for the /c/<text> endpoint."""
    # Replace underscore with a space
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_text_python(text):
    """Route handler for the /python/<text> endpoint."""
    # Replace underscore with a space
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """Route handler for the /number/<n> endpoint."""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    """Route handler for the /number_template/<n> endpoint."""
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_number_odd_or_even(n):
    """Route handler for the /number_odd_or_even/<n> endpoint."""
    return render_template('6-number_odd_or_even.html', number=n,
                           odd_or_even='odd' if n % 2 != 0 else 'even')


if __name__ == '__main__':
    # Run the Flask application on 0.0.0.0:5000
    app.run(host='0.0.0.0', port=5000)
