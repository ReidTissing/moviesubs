from nltk import FreqDist
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
# def spans(txt):
#     tokens=nltk.word_tokenize(txt)
#     offset = 0
#     for token in tokens:
#         offset = txt.find(token, offset)
#         yield token, offset, offset+len(token)
#         offset += len(token)
#
#
# s = "And now for something completely different and."
# for token in spans(s):
#     print(token)
#     assert token[0]==s[token[1]:token[2]]
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
print(words[:100])

freqDist = FreqDist(words)
words = list(freqDist.keys())

print(freqDist.plot(10))


