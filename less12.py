import sqlite3
from bs4 import BeautifulSoup
import requests

# Парсинг сайту
response = requests.get("https://www.bbc.com/ukrainian/features-66330880")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    lisT = soup.find_all("h2", {"tabindex": "-1"})

    # Робота з БД

    db = sqlite3.connect("database.sl3", 5)
    cur = db.cursor()

    # cur.execute("CREATE TABLE final_table (name Text);")
    num = 0
    for i in lisT:
        if num < 10:
            cur.execute("INSERT INTO final_table (name) VALUES (?);", lisT[num].text)
            # cur.execute("DELETE FROM final_table;")
            num += 1

    db.commit()
    db.close()
