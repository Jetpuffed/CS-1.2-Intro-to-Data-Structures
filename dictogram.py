#!usr/bin/env python3
# encoding=utf-8

import random


class Dictogram(object):
    def __init__(self, word_list):
        """Initializes the dictogram properties"""
        self.word_list = word_list
        self.dictionary_histogram = self.build_dictogram()
        self.tokens = sum(self.dictionary_histogram.values())
        self.types = self.unique_words()

    def build_dictogram(self):
        """
        Creates a histogram dictionary using
        the word_list property and returns it.
        """
        dictogram = {}
        for word in self.word_list:
            dictogram[word] = dictogram.get(word, 0) + 1
        return dictogram

    def frequency(self, word):
        """
        Returns the frequency or count of the
        given word in the dictionary histogram.
        """
        if self.dictionary_histogram.get(word) is None:
            return 0
        return self.dictionary_histogram[word]

    def unique_words(self):
        """
        Returns the number of unique
        words in the dictionary histogram.
        """
        return len(self.dictionary_histogram)

    def sample(self):
        """
        Randomly samples from the dictionary
        histogram based on the frequency, returns a word.
        """
        index = random.random()
        count = self.tokens
        probability = 0
        for key in self.dictionary_histogram.keys():
            percent = self.dictionary_histogram[key] / count
            if probability < index <= probability + percent:
                return key
            probability += percent


def print_dictogram(word_list):
    """
    Creates a dictionary based histogram (dictogram)
    and then prints out its properties and samples from it.
    """
    print()
    print("Dictionary Histogram:")
    print("word list: {}".format(word_list))
    # Create a dictogram and display its contents
    dictogram = Dictogram(word_list)
    print("dictogram: {}".format(dictogram.dictionary_histogram))
    print("{} tokens, {} types".format(dictogram.tokens, dictogram.types))
    for word in word_list[-2:]:
        freq = dictogram.frequency(word)
        print("{!r} occurs {} times".format(word, freq))
    print()
    print_dictogram_samples(dictogram)


def print_dictogram_samples(dictogram):
    """Compares sampled frequency to observed frequency"""
    print("Dictionary Histogram samples:")
    # Sample the histogram 10,000 times and count frequency of results
    samples_list = [dictogram.sample() for _ in range(10000)]
    samples_hist = Dictogram(samples_list)
    print("samples: {}".format(samples_hist.dictionary_histogram))
    print()
    print("Sampled frequency and error from observed frequency:")
    header = "| word type | observed freq | sampled freq  |  error  |"
    divider = "-" * len(header)
    print(divider)
    print(header)
    print(divider)
    # Colors for error
    green = "\033[32m"
    yellow = "\033[33m"
    red = "\033[31m"
    reset = "\033[m"
    # Check each word in original histogram
    for word, count in dictogram.dictionary_histogram.items():
        # Calculate word"s observed frequency
        observed_freq = count / dictogram.tokens
        # Calculate word"s sampled frequency
        samples = samples_hist.frequency(word)
        sampled_freq = samples / samples_hist.tokens
        # Calculate error between word"s sampled and observed frequency
        error = (sampled_freq - observed_freq) / observed_freq
        color = green if abs(error) < 0.05 else yellow if abs(error) < 0.1 else red
        print(
            "| {!r:<9} ".format(word)
            + "| {:>4} = {:>6.2%} ".format(count, observed_freq)
            + "| {:>4} = {:>6.2%} ".format(samples, sampled_freq)
            + "| {}{:>+7.2%}{} |".format(color, error, reset),
        )
    print(divider)
    print()


if __name__ == "__main__":
    print_dictogram(
        ["one", "fish", "two", "fish", "red", "fish", "blue", "fish"],
    )
