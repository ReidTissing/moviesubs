from nltk import FreqDist
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import nltk
from pysubparser import parse


file = open("D:\\code\\nltk\\subtitles\\shameless.srt", "rt")
# text = "This is your custom text . You can replace it with anything you want . Feel free to modify it and test ."
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
# print(words[:100])

# freqDist = FreqDist(words)
# words = list(freqDist.keys())
#
# print(freqDist.plot(10))

def getsubtitles():
    subtitles = parse('D:\\code\\nltk\\subtitles\\shameless.srt')
    newsubs = []
    # for subtitle in subtitles:
    #     newsubs.append(subtitle.clean_up(remove_formatting=True, to_lowercase=True))
    # print(newsubs)
    for subtitle in subtitles:
        subtitle.clean_up(remove_formatting=True,to_lowercase=True)
        if "yeah" in str(subtitle):
            newsubs.append('{} - {} > {}'.format(subtitle.start, subtitle.end, subtitle.text))
    print(newsubs[0])



getsubtitles()