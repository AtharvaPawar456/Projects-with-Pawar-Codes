# URL Shortener

import hashlib

def shorten_url(url):
    # Generate MD5 hash of the URL
    md5_hash = hashlib.md5(url.encode()).hexdigest()

    # Take the first 8 characters of the hash as the shortened URL
    short_url = md5_hash[:8]

    return short_url

# Test the URL shortener
long_url = input("Enter the long URL: ")
shortened_url = shorten_url(long_url)
print("Shortened URL:", shortened_url)


'''
=================================
Test Case:
=================================

Enter the long URL: https://www.instagram.com/projects_with_pawar.in/
Shortened URL: d372cf47

'''