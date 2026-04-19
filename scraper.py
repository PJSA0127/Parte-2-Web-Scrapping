import requests, os
from bs4 import BeautifulSoup
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

base_url = "https://quotes.toscrape.com/page/{}/"

quotes_data = []
all_tags = []

page = 1

while True:
    url = base_url.format(page)
    response = requests.get(url)

    if response.status_code != 200:
        break

    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("div", class_="quote")

    if not quotes:
        break

    for quote in quotes:
        text = quote.find("span", class_="text").get_text()
        author = quote.find("small", class_="author").get_text()
        tags = [tag.get_text() for tag in quote.find_all("a", class_="tag")]

        quotes_data.append({
            "text": text,
            "author": author,
            "tags": ", ".join(tags)
        })

        all_tags.extend(tags)

    page += 1

df = pd.DataFrame(quotes_data)

data_folder = "data"

if not os.path.exists(data_folder):
    os.makedirs(data_folder, exist_ok=True)

df["text"] = df["text"].str.replace("“|”", "", regex=True)

df.to_csv(f"{data_folder}/quotes.csv", index=False, encoding="utf-8")

author_counts = df["author"].value_counts().reset_index()
author_counts.columns = ["author", "count"]

author_counts.to_csv(f"{data_folder}/top_authors.csv", index=False)

tag_counts = Counter(all_tags)
tags_df = pd.DataFrame(tag_counts.items(), columns=["tag", "count"])
tags_df = tags_df.sort_values(by="count", ascending=False)

tags_df.to_csv(f"{data_folder}/top_tags.csv", index=False)

print("Scraping y análisis completado")

# GRÁFICA TOP AUTORES
top_authors = author_counts.head(10)

plt.figure()
plt.bar(top_authors["author"], top_authors["count"])
plt.xticks(rotation=45, ha="right")
plt.title("Top 10 Autores con más citas")
plt.xlabel("Autor")
plt.ylabel("Cantidad")

plt.tight_layout()
plt.savefig(f"{data_folder}/top_authors.png")
plt.close()

# GRÁFICA TOP TAGS
top_tags = tags_df.head(10)

plt.figure()
plt.bar(top_tags["tag"], top_tags["count"])
plt.xticks(rotation=45, ha="right")
plt.title("Top 10 Tags más usados")
plt.xlabel("Tag")
plt.ylabel("Cantidad")

plt.tight_layout()
plt.savefig(f"{data_folder}/top_tags.png")
plt.close()

print("Gráficas generadas")