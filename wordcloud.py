from wordcloud import WordCloud
import matplotlib.pyplot as plt
for speech in speeches:
    print(speech)
    speech = open(speech, 'r').read()
    cleaned_speech = remove_punctuation(speech)
    text = cleaned_speech
    wordcloud = WordCloud().generate(text)
# Display the generated image:
    plt.figure( figsize=(20,10) )
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()