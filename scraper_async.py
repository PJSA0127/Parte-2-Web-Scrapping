import asyncio
import aiohttp
from bs4 import BeautifulSoup
from textblob import TextBlob
from sqlalchemy.orm import Session
from models import Quote, Author, Tag

BASE_URL = "https://quotes.toscrape.com/page/{}/"

async def fetch_page(session, page):
    url = BASE_URL.format(page)
    try:
        async with session.get(url) as response:
            if response.status != 200:
                return None
            return await response.text()
    except Exception as e:
        print(f"Error fetching page {page}: {e}")
        return None

def analyze_sentiment(text):
    blob = TextBlob(text)
    score = blob.sentiment.polarity
    if score > 0.1:
        label = "Positivo"
    elif score < -0.1:
        label = "Negativo"
    else:
        label = "Neutral"
    return score, label

async def run_scraper(db: Session):
    async with aiohttp.ClientSession() as session:
        # We can concurrently fetch pages 1 to 20, as the site has around 10 pages.
        tasks = [fetch_page(session, p) for p in range(1, 21)]
        pages_html = await asyncio.gather(*tasks)

        authors_cache = {a.name: a for a in db.query(Author).all()}
        tags_cache = {t.name: t for t in db.query(Tag).all()}

        quotes_added = 0

        for html in pages_html:
            if not html: continue
            
            soup = BeautifulSoup(html, "html.parser")
            quotes = soup.find_all("div", class_="quote")
            if not quotes: continue
            
            for quote_block in quotes:
                text = quote_block.find("span", class_="text").get_text().replace("“", "").replace("”", "")
                author_name = quote_block.find("small", class_="author").get_text()
                tag_elements = quote_block.find_all("a", class_="tag")
                tag_names = [t.get_text() for t in tag_elements]

                # Check if quote exists
                existing_quote = db.query(Quote).filter(Quote.text == text).first()
                if existing_quote:
                    continue

                # Get or Create Author
                if author_name not in authors_cache:
                    new_author = Author(name=author_name)
                    db.add(new_author)
                    db.flush() # get id
                    authors_cache[author_name] = new_author
                
                author_obj = authors_cache[author_name]

                # Get or Create Tags
                quote_tags = []
                for t_name in tag_names:
                    if t_name not in tags_cache:
                        new_tag = Tag(name=t_name)
                        db.add(new_tag)
                        db.flush()
                        tags_cache[t_name] = new_tag
                    quote_tags.append(tags_cache[t_name])
                
                # Sentiment
                score, label = analyze_sentiment(text)

                new_quote = Quote(
                    text=text,
                    author_id=author_obj.id,
                    sentiment_score=score,
                    sentiment_label=label
                )
                
                # Append tags
                for qt in quote_tags:
                    new_quote.tags.append(qt)
                
                db.add(new_quote)
                quotes_added += 1

        db.commit()
        return quotes_added
