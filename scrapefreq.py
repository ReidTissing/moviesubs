import json

import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.probability import *
import csv
import glob, os
import string
from nltk import FreqDist
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt


def getFrequency(moviename, subfilepath):
    file = open(subfilepath, "rt")
    text = file.read()
    file.close()

    # split into words
    tokenized = word_tokenize(text)
    # remove uppercase words, usually sounds
    tokens = []
    for token in tokenized:
        if token.isupper():
            pass
        else:
            tokens.append(token)
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
    # until I implement my own tokenizer, exclude contractions
    # junk_words = ['nt', 'na', 'gon', 'won']
    junk_words = ['nt', 'na', 'gon', 'won', 'got', 'get']
    words = [w for w in words if not w in junk_words]
    # test print first 100 words
    # print(words[:100])
    knowcount = words.count("know")
    return knowcount
    # freqDist = FreqDist(words)


films_dates = {"avengers endgame": "04/26/2019",
               "avengers infinity war": "04/27/2018",
               "bohemian rhapsody": "2/12/2019",
               "fate of the furious": "4/14/2017",
               "fight club": "09/10/1999",
               "jurassic world fallen kingdom": "5/21/2018",
               "midsommar": "7/3/2019",
               "solo": "5/10/2018",
               "star wars force awakens": "12/18/2015",
               "star wars last jedi": "12/15/2017",
               "terminator dark fate": "10/23/2019",
               "the martian": "10/2/2015",
               "thor ragnarok": "11/3/2017",
               "war planet of the apes": "7/14/2017",
               "we bought a zoo": "11/6/2011"}


def traverse():
    os.chdir("D:\\code\\nltk\\subtitles\\")
    for file in glob.glob("*.srt"):
        name = str(file)
        name = name[:-4]
        # print(name)
        print(getFrequency(name, "D:\\code\\nltk\\subtitles\\" + file))


def writejson(distribution):
    with open('data.json', 'w', encoding='utf-8') as f:
        for key, count in distribution.most_common(20):
            json.dump([key, count], f, ensure_ascii=False, indent=4)


# getFrequency("War of the Planet of the Apes", "D:\\code\\nltk\\subtitles\\warapes.srt")
traverse()
