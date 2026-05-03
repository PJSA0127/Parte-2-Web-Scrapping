import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

data = []

for i in range(len(quotes)):
    data.append({
        "frase": quotes[i].text,
        "autor": authors[i].text
    })

df = pd.DataFrame(data)

df.to_csv("quotes.csv", index=False, encoding="utf-8")

print("Datos guardados en quotes.csv")