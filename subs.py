from datetime import time
from moviepy.editor import VideoFileClip, concatenate_videoclips
from pysubparser import parse
#generates output movie based on subtitle input
file = open(".\\subtitles\\Bohemian.Rhapsody.srt", "rt")
text = file.read()
file.close()


def getsubtitles():
    subtitles = parse('.\\subtitles\\Bohemian.Rhapsody.srt')
    newsubs = []
    clips = []

    for subtitle in subtitles:
        subtext = subtitle.clean_up(remove_formatting=True, to_lowercase=True)

        if 'freddie' in subtext:
            t, t2 = subtitle.start, subtitle.end
            newstart = time.isoformat(t)
            newend = time.isoformat(t2)

            clip = VideoFileClip("F:\\Bohemian.Rhapsody.mkv").subclip(newstart, newend)
            clips.append(clip)
            newsubs.append('{} - {} > {}'.format(subtitle.start, subtitle.end, subtext))

    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile("freddie.mp4")
    for subtile in newsubs:
        print(subtile)


getsubtitles()
