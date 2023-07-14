# Web Scraper

import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        # Perform scraping operations on the soup object
        # Example: Extract title and print it
        title = soup.title.text
        print("Title:", title)
    except requests.exceptions.RequestException as e:
        print("Error:", e)

# Test the web scraper
url = input("Enter the URL of the website to scrape: ")
scrape_website(url)


'''
=================================
Test Case:
=================================

Enter the URL of the website to scrape: https://www.instagram.com/projects_with_pawar.in/
Title: ProjectsWith🅿🅰🆆🅰🆁.🅸🅽 (@projects_with_pawar.in) | In
stag

'''