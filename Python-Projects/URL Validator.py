# URL Validator

# pip install validators

import validators

def validate_url(url):
    if validators.url(url):
        print("Valid URL")
    else:
        print("Invalid URL")

# Test the URL Validator
url = input("Enter the URL: ")
validate_url(url)


'''
=================================
Test Case:
=================================

Test1:
Enter the URL: https://www.instagram.com/projects_with_pawar.in/
Valid URL

---------------------------------

Test2:
Enter the URL: hsvdu udeyvi
Invalid URL

'''