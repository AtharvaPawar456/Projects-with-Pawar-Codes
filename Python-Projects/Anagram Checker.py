# Anagram Checker

def is_anagram(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if lengths are equal
    if len(str1) != len(str2):
        return False

    # Sort the characters in both strings
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    # Compare the sorted strings
    if sorted_str1 == sorted_str2:
        return True
    else:
        return False

# Test the anagram checker
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

if is_anagram(word1, word2):
    print("The words are anagrams.")
else:
    print("The words are not anagrams.")


'''
=================================
Test Case:
=================================

Test1:
Enter the first word: listen
Enter the second word: silent
The words are anagrams.

---------------------------------

Test2:
Enter the first word: bad
Enter the second word: hat
The words are not anagrams.

'''