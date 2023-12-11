#!/usr/bin/python3
"""web application script"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route handler for the root path
    returns a greeting message
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    """main method to run the Flask application"""
    app.run(host='0.0.0.0', port=5000)
