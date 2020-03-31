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
    junk_words = ['nt', 'na', 'gon', 'won']
    words = [w for w in words if not w in junk_words]
    # test print first 100 words
    # print(words[:100])

    freqDist = FreqDist(words)
    words = list(freqDist.keys())

    # print(freqDist.plot(10))

    fig = plt.figure(figsize=(10, 4))
    plt.gcf().subplots_adjust(bottom=0.15)  # to avoid x-ticks cut-off
    plt.xlabel('words', fontsize=18)
    plt.ylabel('times said', fontsize=16)
    fdist = FreqDist(freqDist)
    fdist.plot(10, cumulative=False, title="Most Frequently Used Words in " + moviename)
    plt.show()
    # fig.suptitle('test title', fontsize=20)
    fig.savefig(moviename + '.png', bbox_inches="tight")


getFrequency("Solo: A Star Wars Story", "D:\\code\\nltk\\subtitles\\Solo.srt")
