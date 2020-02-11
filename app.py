#!/usr/bin/env python3
# encoding=utf-8

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "A randomly generated sentence will go here."


if __name__ == "__main__":
    app.run()
