from moviepy.editor import *
from moviepy.editor import VideoFileClip, concatenate_videoclips

clip3 = VideoFileClip("yeahs.mp4")
# clip.write_videofile("share.mp4")

clip1 = VideoFileClip("yeah2.mp4")
clip2 = VideoFileClip("yeah3.mp4")

final_clip = concatenate_videoclips([clip1,clip2,clip3])
final_clip.write_videofile("first3.mp4")