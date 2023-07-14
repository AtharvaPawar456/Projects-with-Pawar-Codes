# Phone Number Validator

import re

def is_valid_phone_number(phone_number):
    # Remove all non-digit characters
    cleaned_number = re.sub(r'\D', '', phone_number)

    # Check if the cleaned number has 10 digits
    if len(cleaned_number) == 10:
        return True
    else:
        return False

# Test the phone number validator
number = input("Enter a phone number: ")

if is_valid_phone_number(number):
    print("The phone number is valid.")
else:
    print("The phone number is invalid.")


'''
=================================
Test Case:
=================================

Test1:
Enter a phone number: 91 99999 11111
The phone number is invalid.

---------------------------------

Test2:
Enter a phone number: 1111111111
The phone number is valid.

'''