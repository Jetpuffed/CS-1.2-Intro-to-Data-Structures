#!/usr/bin/env python3
# encoding=utf-8

from flask import Flask

from dictionary_words import generate

app = Flask(__name__)


@app.route("/")
def index():
    return generate(10)


if __name__ == "__main__":
    app.run()
