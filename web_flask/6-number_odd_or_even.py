#!/usr/bin/python3


"""
This module defines a Flask application with a single route.
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    Display 'Hello HBNB!' when accessing the root route.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Display 'HBNB'.
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_C(text):
    """
    Display 'C' followed by the value of the text variable
    (replace underscore _ symbols with a space )
    """
    message = "C " + text.replace("_", " ")
    return message


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_Python(text):
    """
    Display 'Python' followed by the value of the text variable
    (replace underscore _ symbols with a space )
    """
    message = "Python " + text.replace("_", " ")
    return message


@app.route('/number/<int:n>', strict_slashes=False)
def display_n(n):
    """
    Display 'n' followed by "is a number"
    only if n is an integer
    """
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    """
    Display a template with {{ number }} = 'n'
    only if n is an integer
    """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_number_odd_or_even(n):
    """
    Display a template with {{ number }} = 'n'
    only if n is an integer
    """
    if n % 2 == 0:
        o_or_e = 'even'
    else:
        o_or_e = 'odd'
    page = '6-number_odd_or_even.html'
    return render_template(page, number=n, odd_or_even=o_or_e)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
