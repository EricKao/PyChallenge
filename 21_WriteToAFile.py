# This program parse all heading content and output to a file of HTML page
# by using requests and BeautifulSoup module
#
# Created by Eric

import requests
from bs4 import BeautifulSoup


def main():
    # Get file name
    FileName = raw_input("Please input your file name: ")

    # Using requests module to get url request
    Url = 'http://www.nytimes.com'
    r = requests.get(Url)

    # Using BeautifulSoup to parse response html
    Soup = BeautifulSoup(r.text, "html.parser")

    # Print out all story-heading line text
    with open(FileName, 'w') as open_file:
        for story_heading in Soup.find_all(class_="story-heading"):
            if story_heading.a:
                open_file.write(story_heading.a.text.encode("utf-8").replace("\n", " ").strip() + '\n')
            else:
                open_file.write(story_heading.contents[0].encode("utf-8").strip() + '\n')

if __name__ == "__main__":
    main()
