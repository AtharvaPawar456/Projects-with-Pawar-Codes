# Word Counter

def count_words(text):
    # Split the text into words using 
    # whitespace as the delimiter
    words = text.split()

    # Return the count of words
    return len(words)

# Test the word counter
input_text = input("Enter a sentence or text: ")
word_count = count_words(input_text)
print("Number of words:", word_count)


'''
=================================
Test Case:
=================================

Enter a sentence or text: eisbisb asicsieg sedgsdeig  scduge 
Number of words: 4

'''