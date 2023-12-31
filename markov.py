"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    string = open("green-eggs.txt").read()
    

    return string


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

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

    list_of_words = text_string.split()

    word_list =[]

    for i in range(len(list_of_words)-2): 
        tuple_of_list = (list_of_words[i],list_of_words[i+1])
        value_of_list = list_of_words[i+2]

        if tuple_of_list not in chains: 
            chains[tuple_of_list] = [value_of_list]

        else:
            chains[tuple_of_list].append(value_of_list)

    print(chains)


        #assess 
    #     if chains.get()
    #     chains[(list_of_words[i],list_of_words[i+1])] = [list_of_words[i+2]] #think of this as labeling empty tupperware
    # print(chains)

    #tuple created
    #access the value with i+2
    #if the key isn't in the dictionary, you'll create it and append
    #if already in dict, you'll append the value



    return word_list


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)

# print(open_and_read_file("green-eggs.txt"))

print(make_chains(open_and_read_file("green-eggs.txt")))
