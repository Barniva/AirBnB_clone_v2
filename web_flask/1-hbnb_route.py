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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
