#!/usr/bin/python3
"""flask class"""
from flask import Flask
"""Flask class"""


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def helo_hbnb():
    """displays text
    Returns:
        text
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def disp_hbnb():
    """displays text
    Returns:
        text
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def disp_C(text):
    """displays text
    Args:
        text (str): text
    Returns:
        text
    """
    return 'C %s' % text.replace('_', ' ')


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def disp_python(text):
    """displays text
    Args:
        text (str): text
    Returns:
        text
    """
    return 'Python %s' % text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
