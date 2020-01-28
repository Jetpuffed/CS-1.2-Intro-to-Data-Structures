# file_words = open("text.txt", "r")
# lines_words = file_words.readlines()
source = []
with open("text.txt", "r") as _:
    for line in _:
        for word in line.split():
            source.append(word)


def histogram(source_text):
    """Builds a histogram from a data set."""
    histogram = {}
    for _ in source_text:
        if histogram.get(_) is None:
            n = source_text.count(_)
            histogram[_] = n
        else:
            continue
    return histogram


def unique_words(histogram):
    """Reads a histogram and counts the amount of keys."""
    return len(histogram)


def frequency(word, histogram):
    """Takes a word and a histogram and returns
    the number of times the word was detected."""
    if histogram.get(word) is None:
        return "Word not found."
    else:
        return f"Word has been used {histogram[word]} times."
