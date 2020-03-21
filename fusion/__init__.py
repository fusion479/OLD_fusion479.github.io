from flask import Flask, render_template, request, redirect, url_for, session, flash
from functools import wraps
from google.cloud import firestore
import json
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

file = os.path.dirname(os.path.abspath(__file__))


@app.route('/')
def root():
    return render_template(
        'index.html'
    )


if __name__ == "__main__":
    app.debug = True
    app.run()
