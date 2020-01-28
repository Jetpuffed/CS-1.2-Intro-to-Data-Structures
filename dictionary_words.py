import random
import sys

num = sys.argv[1:]

file_words = open("/usr/share/dict/words", "r")
lines_words = file_words.readlines()
sentence = []

i = 0
while i < int(num[0]):
    if i != int(num[0]):
        random_index = random.randint(0, len(lines_words) - 1)
        sentence.append(lines_words[random_index].strip())
        i += 1

print(" ".join(sentence))
