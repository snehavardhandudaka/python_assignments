import feedparser

def fetch_rss_feed(url):
    feed = feedparser.parse(url)
    for entry in feed.entries:
        print(f"Title: {entry.title}")
        print(f"Link: {entry.link}")
        print(f"Published: {entry.published}")
        print()

url = input("Enter the RSS feed URL: ")
fetch_rss_feed(url)
