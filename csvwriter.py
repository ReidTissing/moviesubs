import json

import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.probability import *
import csv

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
            print(token)
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
    #until I implement my own tokenizer, exclude contractions
    #junk_words = ['nt', 'na', 'gon', 'won']
    junk_words = ['nt','na','gon','won','got','get']
    words = [w for w in words if not w in junk_words]
    # test print first 100 words
    # print(words[:100])

    freqDist = FreqDist(words)



    # file = csv.writer(open('word_frequencies.csv', 'w'))
    # for key, count in freqDist.most_common(200):
    #     line = "['" + str(key) + "' , " + str(count) + "'],"
    #     print(line)
    #     file.writerow(line)

    # with open('eggs.csv', 'w', newline='') as csvfile:
    #     spamwriter = csv.writer(csvfile, delimiter=' ',
    #                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #     for key, count in freqDist.most_common(200):
    #         spamwriter.writerow([key,count])

    with open('data.json', 'w', encoding='utf-8') as f:
        for key, count in freqDist.most_common(20):
            json.dump([key,count], f, ensure_ascii=False, indent=4)

getFrequency("War of the Planet of the Apes", "D:\\code\\nltk\\subtitles\\warapes.srt")
