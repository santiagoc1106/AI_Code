import requests
from bs4 import BeautifulSoup

url = 'https://open.spotify.com/search'
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
search = soup.find("div", class_ = "search")
print(page.text)