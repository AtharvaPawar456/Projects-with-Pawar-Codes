# Word Cloud Generator

from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_word_cloud(text):
    # Create a WordCloud object
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    # Display the word cloud using matplotlib
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

# Test the word cloud generator
text = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Sed at odio lobortis, volutpat velit nec, lacinia tortor.
Curabitur condimentum felis eu ante auctor, ac consequat lorem congue.
Donec ultricies tellus id velit gravida, ac eleifend odio suscipit.
Projects_with_pawar.in, Projects_with_pawar.in Projects_with_pawar.in Projects_with_pawar.in Projects_with_pawar.in Projects_with_pawar.in
Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.
'''

generate_word_cloud(text)
