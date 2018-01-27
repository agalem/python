"Laboratorium 4, Agnieszka Lempaszek"

import codecs, re

# Funkcje pomocnicze

def _words_from_line(line):

    words = re.split('[\W\d]+', line)
    return [w.lower() for w in words if w]

def _sort_stat(stat):
    return sorted(stat, key=lambda p: p[1], reverse=True)


# Zadanie 4.1

def invert(in_filename, out_filename):
    input_file  = open(in_filename, 'r')
    output_file = open(out_filename, 'w')

    output_file.write(input_file.read()[::-1])

    input_file.close()
    output_file.close()

invert('inverted.txt', 'wiki10.txt')

# Zadanie 4.2

def unique_words(filename):
    f = open(filename, 'r')
    wordset = set()

    for line in f:
        wordset |= set(_words_from_line(line))

    wordlist = list(wordset)

    return sorted(wordlist)

print (unique_words('wiki10.txt'))

# Zadanie 4.3

def word_stat(filename):
    f = open(filename, 'r')
    words = []
    dictionary = {}

    

#print (word_stat('wiki10.txt'))
