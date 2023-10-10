import requests
import bs4
from bs4 import BeautifulSoup

url = "https://www.python.org/"
page = bs4.BeautifulSoup(requests.get(url).text,'lxml')
print(page)
soup = BeautifulSoup(page.text, 'html.parser')
print(soup)

d = {}
for line in soup:
    line = line.strip()
    line = line.lower()
    words = line.split(" ")

    for word in words:
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1
for key in list(d.keys()):
    print(key, ":", d[key])