from flask import Flask, jsonify
from flask import render_template, request
from flask import current_app, abort
import random

# Initialize the Flask application
app = Flask(__name__)


@app.route('/')
def main():
    return "<center><h1>Hej, v'a'rlden!</h1></center>"


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=8080,
        debug=True
    )
