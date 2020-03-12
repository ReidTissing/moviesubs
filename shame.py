import re
file = open("D:\\code\\nltk\\subtitles\\shameless.srt", "rt")
# text = "This is your custom text . You can replace it with anything you want . Feel free to modify it and test ."
text = file.read()
file.close()
re.findall('^(.*)$\n^.*$\naddress 127.0.0.1',text, re.MULTILINE)