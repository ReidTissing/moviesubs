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


# print(words[:100])

# freqDist = FreqDist(words)
# words = list(freqDist.keys())
#
# print(freqDist.plot(10))

def getsubtitles():
    subtitles = parse('D:\\code\\nltk\\subtitles\\shameless.srt')
    newsubs = []
    clips = []

    # for subtitle in subtitles:
    #     newsubs.append(subtitle.clean_up(remove_formatting=True, to_lowercase=True))
    # print(newsubs)


    #
    for subtitle in subtitles:
        subtext = subtitle.clean_up(remove_formatting=True, to_lowercase=True)
    #     subtitle.clean_up(remove_formatting=True,to_lowercase=True)
    #     if "yeah" in str(subtitle).lower():
        if 'yeah' in subtext:
            t,t2 = subtitle.start,subtitle.end
            newstart = time.isoformat(t)
            newend = time.isoformat(t2)



            clip = VideoFileClip("Shameless.1.mkv").subclip(newstart, newend)
            clips.append(clip)
            newsubs.append('{} - {} > {}'.format(subtitle.start, subtitle.end, subtext))


    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile("my_concatenation.mp4")
    for subtile in newsubs:
        print(subtile)


getsubtitles()