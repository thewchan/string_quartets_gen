"""Temporary one-page web app for string quartet generator."""
from flask import Flask, flash, redirect, request, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)
ALLOWED_EXTENSIONS = {'mid', 'midi'}


@app.route('/index')
def index():
    """Temporary home page for string quartet web-app."""
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
