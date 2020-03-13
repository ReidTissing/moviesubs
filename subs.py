from nltk import FreqDist
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import nltk
from pysubparser import parse
from moviepy.editor import *
from moviepy.editor import VideoFileClip, concatenate_videoclips
from datetime import datetime, date, time, timedelta
from dateutil import relativedelta


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
    clipcounter = 0
    # for subtitle in subtitles:
    #     newsubs.append(subtitle.clean_up(remove_formatting=True, to_lowercase=True))
    # print(newsubs)
    for subtitle in subtitles:
        subtitle.clean_up(remove_formatting=True,to_lowercase=True)
        if "yeah" in str(subtitle):
            t,t2 = subtitle.start,subtitle.end
            newstart = time.isoformat(t)
            newend = time.isoformat(t2)


            print("newend")
            clip3 = VideoFileClip("Shameless.1.mkv").subclip(newstart, newend)
            #
            final_clip = concatenate_videoclips([clip3])
            final_clip.write_videofile("my_concatenation.mp4")
            newsubs.append('{} - {} > {}'.format(subtitle.start, subtitle.end, subtitle.text))
    i = 0
    while( i < len(newsubs)):
        print(newsubs[i])
        i = i+1


# clip.write_videofile("share.mp4")
#
# clip1 = VideoFileClip("share.mp4")
# clip2 = VideoFileClip("shameless.mp4").subclip(6, 8)

getsubtitles()