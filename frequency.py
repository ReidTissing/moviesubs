#!/usr/bin/python

import string
from nltk import FreqDist
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import sys, getopt


def analyze(inputfile):

    file = open(inputfile, "rt")

    text = file.read()
    file.close()

    # split into words
    tokens = word_tokenize(text)
    # convert to lower case
    tokens = [w.lower() for w in tokens]
    # remove punctuation from each word
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in tokens]
    # remove remaining tokens that are not alphabetic
    words = [word for word in stripped if word.isalpha()]
    # filter out stop words
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if not w in stop_words]
    junk_words = ['nt']
    words = [w for w in words if not w in junk_words]
    print(words[:100])

    freqDist = FreqDist(words)
    words = list(freqDist.keys())

    print(freqDist.plot(50))


def main(argv):
    inputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:", ["ifile="])
    except getopt.GetoptError:
        print('freqency.py -i <inputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('frequency.py -i <inputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
    print('Input file is "', inputfile)
    analyze(inputfile)



if __name__ == "__main__":
    main(sys.argv[1:])
