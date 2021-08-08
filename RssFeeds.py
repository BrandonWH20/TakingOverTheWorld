import ssl

import feedparser

# Written to Give us text data to be imported to Knime workspace.
# TODO: 1. Get RSS feed
# TODO: 2. Format data to be read by algorithm.


url="http://www.marketwatch.com/rss/topstories"
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context
feed = feedparser.parse(url) #<<WORKS!!

# TODO: 1. Get_feed: Given a RSS link, will return the feed as a dictionary
def get_feed(url="http://www.marketwatch.com/rss/topstories"):
    feed = feedparser.parse(url)
    return feed


# TODO: 2. Format Data to be read by Knime.
def format(feed = "NULL"):
    return
