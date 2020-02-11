#!/usr/bin/env python3
# encoding=utf-8

import random
import sys

args = sys.argv[1:]


def get_word():
    return random.choice(args)


def get_probability():
    lst = []
    size = 10000
    while len(lst) <= size:
        lst.append(get_word())
    for word in args:
        percent = lst.count(word)
        print("{0} => {1}".format(word, (percent / size) * 100))


if __name__ == "__main__":
    print(get_probability())
