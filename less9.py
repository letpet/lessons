import requests
from bs4 import BeautifulSoup

response = requests.get("https://coinmarketcap.com")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    lisT = soup.find_all("a", {"href": "/currencies/bitcoin/#markets"})
    for i in lisT:
        print(i.text)

print("")

response = requests.get("https://sinoptik.ua")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    lisT = soup.find_all("div", {"class": "main loaded", "id": "bd1"})
    for i in lisT:
        print(i.text)
    lisT = soup.find_all("div", {"class": "main", "id": "bd2"})
    for i in lisT:
        print(i.text)
    lisT = soup.find_all("div", {"class": "main", "id": "bd3"})
    for i in lisT:
        print(i.text)
    lisT = soup.find_all("div", {"class": "main", "id": "bd4"})
    for i in lisT:
        print(i.text)
    lisT = soup.find_all("div", {"class": "main", "id": "bd5"})
    for i in lisT:
        print(i.text)
    lisT = soup.find_all("div", {"class": "main", "id": "bd6"})
    for i in lisT:
        print(i.text)
    lisT = soup.find_all("div", {"class": "main", "id": "bd7"})
    for i in lisT:
        print(i.text)
