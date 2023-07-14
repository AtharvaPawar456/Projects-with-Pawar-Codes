# Text Translator

# pip install googletrans==4.0.0-rc1

from googletrans import Translator

def translate_text(text, source_lang, target_lang):
    translator = Translator()
    translated = translator.translate(text, src=source_lang, dest=target_lang)
    return translated.text

# Test the Text Translator
text = input("Enter the text to translate: ")
source_lang = input("Enter the source language (e.g., 'en' for English): ")
target_lang = input("Enter the target language (e.g., 'fr' for French): ")

translated_text = translate_text(text, source_lang, target_lang)
print("Translated text:", translated_text)


'''
=================================
Test Case:
=================================

Enter the text to translate: Python is a high-level, general-purpose programming language
Enter the source language (e.g., 'en' for English): en
Enter the target language (e.g., 'fr' for French): fr
Translated text: Python est un langage de programmation à usage général de haut niveau

'''