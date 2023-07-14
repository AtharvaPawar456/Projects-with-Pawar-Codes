# Website Performance Analyzer

import requests
from datetime import datetime

def analyze_website_performance(url):
    try:
        # Make a GET request to the URL
        start_time = datetime.now()
        response = requests.get(url)
        end_time = datetime.now()

        # Calculate response time
        response_time = end_time - start_time

        # Print performance metrics
        print("Website Performance Analysis:")
        print("URL:", url)
        print("Response Time:", response_time)
        print("Status Code:", response.status_code)
        print("Content Length:", len(response.content), "bytes")
    except requests.exceptions.RequestException as e:
        print("Error occurred while analyzing website performance:", str(e))

# Test the Website Performance Analyzer
url = input("Enter the URL to analyze: ")
analyze_website_performance(url)


'''
=================================
Test Case:
=================================

Enter the URL to analyze: https://www.instagram.com/projects_with_pawar.in/
Website Performance Analysis:
URL: https://www.instagram.com/projects_with_pawar.in/
Response Time: 0:00:00.893244
Status Code: 200
Content Length: 331965 bytes


'''