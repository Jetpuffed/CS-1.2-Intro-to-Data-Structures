#!/usr/bin/env python3
# encoding=utf-8

from flask import Flask

from markov import MarkovChain

app = Flask(__name__)


@app.route("/")
def index():
    markov = MarkovChain(
        ["one", "fish", "two", "fish", "red", "fish", "blue", "fish"],
    )
    return markov.walk(10)


if __name__ == "__main__":
    app.run()
