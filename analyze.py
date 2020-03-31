import string
from nltk import FreqDist
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt

def getFrequency(subfilepath, outputimg):
    file = open(subfilepath, "rt")

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
    junk_words = ['nt', 'get']
    words = [w for w in words if not w in junk_words]
    #test print first 100 words
    # print(words[:100])

    freqDist = FreqDist(words)
    words = list(freqDist.keys())

    # print(freqDist.plot(10))

    fig = plt.figure(figsize = (10,4))
    plt.gcf().subplots_adjust(bottom=0.15) # to avoid x-ticks cut-off
    plt.xlabel('words', fontsize=18)
    plt.ylabel('times said', fontsize=16)
    fdist = FreqDist(freqDist)
    fdist.plot(10, cumulative=False, title="Most Frequently Used Words in Jurassic Park World")
    plt.show()
    # fig.suptitle('test title', fontsize=20)
    fig.savefig(outputimg + '.png', bbox_inches = "tight")

getFrequency("D:\\code\\nltk\\subtitles\\jwworld.srt","jworld")

