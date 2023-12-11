#!/usr/bin/python3
"""a sccript tu run a web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """root path"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """path hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """handles the C path"""
    formatted_text = text.replace("_", " ")
    return f"C {formatted_text}"


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def display_python(text="is cool"):
    """handles the python path"""
    return f"python {text.replace('_', ' ')}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
