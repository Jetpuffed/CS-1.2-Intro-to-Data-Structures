#!/usr/bin/env python3
# encoding=utf-8

from dictogram import Dictogram


class MarkovChain(object):
    def __init__(self, word_list):
        # The Markov chain will be a dictionary of dictionaries
        # Example: for "one fish two fish red fish blue fish"
        # {"one": {fish:1}, "fish": {"two":1, "red":1, "blue":1}, "two": {"fish":1}, "red": {"fish":1}, "blue": {"fish:1"}}
        self.markov_chain = self.build_markov(word_list)
        self.first_word = list(self.markov_chain.keys())[0]

    def build_markov(self, word_list):
        markov_chain = {}
        for i in range(len(word_list) - 1):
            # Get the current word and the word after
            current_word = word_list[i]
            next_word = word_list[i + 1]
            if current_word in markov_chain.keys():  # Already there
                # Get the histogram for that word in the chain
                histogram = markov_chain[current_word]
                # Add to count
                histogram.dictionary_histogram[next_word] = histogram.dictionary_histogram.get(next_word, 0) + 1
            else:  # First entry
                markov_chain[current_word] = Dictogram([next_word])
        return markov_chain

    def walk(self, num_words):
        first = self.first_word
        sentence = ""
        sentence += first
        word = first
        for _ in range(1, num_words):
            word = Dictogram(self.markov_chain).sample()
            sentence += " {}".format(word)
        return sentence

    def print_chain(self):
        for word, histogram in self.markov_chain.items():
            print(word, histogram.dictionary_histogram)


if __name__ == "__main__":
    markov_chain = MarkovChain(["one", "fish", "two", "fish", "red", "fish", "blue", "fish"])
    markov_chain.print_chain()
    print(markov_chain.walk(10))
