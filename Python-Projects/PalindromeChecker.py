def is_palindrome(string):
    # Remove whitespace and convert to lowercase
    string = string.replace(" ", "").lower()
    
    # Check if the string is equal to its reverse
    if string == string[::-1]:
        return True
    else:
        return False

# Test the function
input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("Palindrome!")
else:
    print("Not a palindrome.")
