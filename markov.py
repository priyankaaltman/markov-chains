"""Generate Markov text from text files."""

from random import choice

import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file = open(file_path).read()

    return file


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words = text_string.split()  # list of words

    for i in range(len(words)-2):

        # if key not in dictionary
        the_tuple = (words[i], words[i+1])
        value = [words[i + 2]]

        chains[the_tuple] = chains.get(the_tuple, []) + value

    return chains


def make_text(chains):
    """Return text from chains."""

    key = choice(list(chains))  # chooses random key to start

    output = list(key)

    while key in chains:

        following_word = choice(chains[key])  # chooses random value

        output.append(following_word)
        key = (key[-1], following_word)  # increments the keys, but one word

    return " ".join(output)


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)


# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
