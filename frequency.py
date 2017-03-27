""" Analyzes the word frequencies in a book downloaded from
Project Gutenberg """

import string
import re


def get_word_list(file_name, n):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    f = open(file_name, 'r')
    text = f.read()
    ls = re.compile('\w+').findall(text)
    return(get_top_n_words(ls, n))


def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequentlyoccurring
    """
    words = []
    frequency = []
    for i in word_list:
        i = str.lower(i)
        if i not in words:
            words.append(i)
    for word in words:
        freq = 0
        for sample in word_list:
            if word == sample:
                freq = freq + 1
        frequency.append(freq)

    d = {}
    for i, word in enumerate(words):
        d[frequency[i]] = word
    return sort_dictionary(d, n)


def sort_dictionary(dictionary, n):
    keys = dictionary.keys()
    keys = sorted(keys)
    word_list = []
    for key in keys:
        word_list.append(dictionary.get(key))
    word_list = word_list[::-1]
    word_list = word_list[:n]
    return word_list




if __name__ == "__main__":
    print("Running WordFrequency Toolbox")
    print(string.punctuation)
    print(get_word_list('english.txt', 5))
