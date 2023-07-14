# RSS Feed Reader

# pip install feedparser

import feedparser

def read_rss_feed(file_path):
    # Parse the RSS feed
    feed = feedparser.parse(file_path)

    # Print the feed title and description
    print("Title:", feed.feed.title)
    print("Description:", feed.feed.description)

    # Print the latest articles
    print("\nLatest Articles:")
    for entry in feed.entries:
        print("-" * 20)
        print("Title:", entry.title)
        print("Link:", entry.link)
        print("Description:", entry.description)

# Test the RSS feed reader
feed_file = "rsstest.xml"
read_rss_feed(feed_file)

'''
=================================
Test Case:
=================================

Title: Apple RSS feed
Description: This RSS feed is about Apple products

Latest Articles:
--------------------
Title: Apple iPhone
Link: http://example.com/iphone/
Description: The iPhone is a line of smartphones designed and marketed by Apple Inc
--------------------
Title: Apple MacBook
Link: http://example.com/macbook/
Description: The MacBook is a brand of Macintosh notebook computers designed and marketed by Apple Inc

'''