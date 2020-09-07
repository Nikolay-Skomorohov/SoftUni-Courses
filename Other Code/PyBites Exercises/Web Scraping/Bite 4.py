import os
from collections import Counter
import urllib.request
from bs4 import BeautifulSoup

# prep
tempfile = os.path.join('/tmp', 'feed')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/feed',
    tempfile
)

with open(tempfile) as f:
    content = f.read().lower()


def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    result = Counter()
    soup = BeautifulSoup(content, 'html.parser')
    tags_list = soup.find_all('category')
    for tag in tags_list:
        if not result[tag.get_text()]:
            result[tag.get_text()] = 1
        else:
            result[tag.get_text()] += 1
    return result.most_common(n)
