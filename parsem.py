from moviepy.editor import *
from moviepy.editor import VideoFileClip, concatenate_videoclips

clip3 = VideoFileClip("shameless.mp4").subclip(3,5)
# clip.write_videofile("share.mp4")

clip1 = VideoFileClip("share.mp4")
clip2 = VideoFileClip("shameless.mp4").subclip(6,8)

final_clip = concatenate_videoclips([clip1,clip2,clip3])
final_clip.write_videofile("my_concatenation.mp4")