import urllib.request
import requests
from bs4 import BeautifulSoup

opener = urllib.request.build_opener()
response = opener.open("https://itstep.org")
print(response.read())

response = requests.get("https://itstep.org")
print(response.text)
