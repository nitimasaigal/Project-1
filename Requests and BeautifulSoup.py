import requests
from bs4 import BeautifulSoup

url = 'http://www.python.org/'
page = requests.get(url)
page.status_code
page.text


soup = BeautifulSoup(page.text, 'html.parser')
soup.text

data = soup.text.replace('\n', '')
data

from collections import Counter
Counter(data.split()).most_common()

