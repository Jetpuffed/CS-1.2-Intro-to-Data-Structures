#!/usr/bin/env python3
# encoding=utf-8

import sys

args = sys.argv[1:]


class Histogram(object):
    def __init__(self):
        self.source = []

    def write_source(self):
        with open("text.txt", "r") as txt:
            for line in txt:
                for word in line.split():
                    self.source.append(word)

    def read_histogram(self):
        dictionary = {}
        for key in self.source:
            if dictionary.get(key) is None:
                count = self.source.count(key)
                dictionary[key] = count
        return dictionary

    def get_unique_words(self, histogram):
        return "Total unique words: {0}".format(len(histogram))

    def get_frequency(self, key, histogram):
        if histogram.get(key) is None:
            return "Word not found."
        return "Word has been used {0} times.".format(histogram[key])


if __name__ == "__main__":
    app = Histogram()
    app.write_source()
    histogram = app.read_histogram()
    print(app.get_unique_words(histogram))
    print(app.get_frequency(args[0], histogram))
