#!/usr/bin/env python3
# encoding=utf-8

import random
import sys

arg = sys.argv[1:]

with open("/usr/share/dict/words", "r") as file_words:
    lines_words = file_words.readlines()
    sentence = []

    index = 0
    while index < int(arg[0]):
        if index != int(arg[0]):
            random_index = random.randint(0, len(lines_words) - 1)
            sentence.append(lines_words[random_index].strip())
            index += 1

    print(" ".join(sentence))
