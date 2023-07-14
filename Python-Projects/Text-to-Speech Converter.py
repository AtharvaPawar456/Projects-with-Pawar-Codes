# Text-to-Speech Converter

# pip install gtts

from gtts import gTTS
import tempfile
import os

def convert_text_to_speech(text, language='en'):
    tts = gTTS(text=text, lang=language)
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_filename = temp_file.name + ".mp3"
    tts.save(temp_filename)
    return temp_filename

# Test the text-to-speech converter
text = input("Enter the text: ")
output_file = convert_text_to_speech(text)

# Save the audio file as "outputaudio.mp3" in the current directory
output_filename = "outputaudio.mp3"
os.rename(output_file, output_filename)
print("Audio file saved as:", output_filename)


'''
=================================
Test Case:
=================================

Enter the text: Hello, how are you
Audio file saved as: outputaudio.mp3

'''