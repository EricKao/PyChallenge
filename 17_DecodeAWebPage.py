# This program randomly generate password for user
#
# Created by Eric

import requests
from bs4 import BeautifulSoup

# Using requests module to get url request
Url = 'http://www.nytimes.com'
r = requests.get(Url)

# Using BeautifulSoup to parse response html
Soup = BeautifulSoup(r.text, "html.parser")

# Print out all story-heading line text
for story_heading in Soup.find_all(class_="story-heading"):
    if story_heading.a:
        print (story_heading.a.text.encode("utf-8").replace("\n", " ").strip())
    else:
        print (story_heading.contents[0].encode("utf-8").strip())
