from datetime import time
from moviepy.editor import VideoFileClip, concatenate_videoclips
from pysubparser import parse
import sys, getopt
# file = open("D:\\code\\nltk\\subtitles\\shameless.srt", "rt")
# # text = "This is your custom text . You can replace it with anything you want . Feel free to modify it and test ."
# text = file.read()
# file.close()


def getsubtitles(inputfile, keyword, outputfile):
    subtitles = parse(inputfile)
    newsubs = []
    clips = []

    for subtitle in subtitles:
        subtext = subtitle.clean_up(remove_formatting=True, to_lowercase=True)

        if keyword in subtext:
            t, t2 = subtitle.start, subtitle.end
            newstart = time.isoformat(t)
            newend = time.isoformat(t2)

            clip = VideoFileClip("tmp.mkv").subclip(newstart, newend)
            clips.append(clip)
            newsubs.append('{} - {} > {}'.format(subtitle.start, subtitle.end, subtext))

    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile(outputfile)
    for subtile in newsubs:
        print(subtile)



def main(argv):
    inputfile = ''
    outputfile = ''
    keyword = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:k:", ["ifile=","ofile=","keywords="])
    except getopt.GetoptError:
        print('generate.py -i <inputfile> -o ')
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