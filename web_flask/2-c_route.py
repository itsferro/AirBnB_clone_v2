#!/usr/bin/python3


"""
This module defines a Flask application with a single route.
"""
from flask import Flask

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
    Display 'HBNB' when accessing the root route.
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_C(text):
    """
    Display 'C' followed by the value of the text variable
    (replace underscore _ symbols with a space )
    when accessing the root route.
    """
    message = "C " + text.replace("_", " ")
    return message


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
