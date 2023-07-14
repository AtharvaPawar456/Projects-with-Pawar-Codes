# Morse Code Translator

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-',
    ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-',
    '@': '.--.-.', ' ': '/'
}


def text_to_morse(text):
    morse_code = []
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
    return ' '.join(morse_code)


def morse_to_text(morse_code):
    text = ''
    morse_code = morse_code.split(' ')
    for morse in morse_code:
        for key, value in MORSE_CODE_DICT.items():
            if value == morse:
                text += key
    return text


# Test the Morse Code Translator
text = input("Enter the text to convert to Morse code: ")
morse_code = text_to_morse(text)
print("Morse Code:", morse_code)

morse_input = input("Enter the Morse code to convert to text: ")
text_output = morse_to_text(morse_input)
print("Text:", text_output)



'''
=================================
Test Case:
=================================

Test1:
Enter the text to convert to Morse code: hello
Morse Code: .... . .-.. .-.. ---
Enter the Morse code to convert to text: .... . .-.. .-.. ---
Text: HELLO

---------------------------------

Test2:
Enter the text to convert to Morse code: hello projects_with_pawar
Morse Code: .... . .-.. .-.. --- / .--. .-. --- .--- . -.-. - ... ..--.- .-- .. - .... ..--.- .--. .- .-- .- .-.
Enter the Morse code to convert to text: .... . .-.. .-.. --- / .--. .-. --- .--- . -.-. - ... ..--.- .-- .. - .... ..--.- .--. .- .-- .- .-.
Text: HELLO PROJECTS_WITH_PAWAR

'''