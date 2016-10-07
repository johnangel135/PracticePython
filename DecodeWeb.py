import requests
from bs4 import BeautifulSoup


def decode() -> object:
    string = []
    base_url = 'http://www.nytimes.com'
    r = requests.get(base_url)
    soup = BeautifulSoup(r.text,"html.parser")
    for story_heading in soup.find_all(class_="story-heading"):
        if story_heading.a:
            # print(story_heading.a.text.replace("\n", " ").strip())
            string.append(story_heading.a.text.replace("\n", " ").strip())
        else:
            # print(story_heading.contents[0].strip())
            string.append(story_heading.contents[0].strip())
    return "\n".join(string)

