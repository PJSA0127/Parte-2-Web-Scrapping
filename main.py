from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from sqlalchemy import func
from database import engine, get_db
import models
from scraper_async import run_scraper

# Create DB tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Web Scraper Analyzer")

# Mount static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return FileResponse("static/index.html")

@app.post("/api/scrape")
async def trigger_scrape(db: Session = Depends(get_db)):
    try:
        quotes_added = await run_scraper(db)
        return {"status": "success", "message": f"Scraping completado. Citas nuevas agregadas: {quotes_added}."}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.get("/api/stats")
def get_stats(db: Session = Depends(get_db)):
    # 1. Top 10 Autores
    top_authors = db.query(models.Author.name, func.count(models.Quote.id).label('total_quotes'))\
                    .join(models.Quote)\
                    .group_by(models.Author.id)\
                    .order_by(func.count(models.Quote.id).desc())\
                    .limit(10).all()
    
    # 2. Top 10 Tags
    top_tags = db.query(models.Tag.name, func.count(models.quote_tag_association.c.quote_id).label('total_quotes'))\
                 .join(models.quote_tag_association)\
                 .group_by(models.Tag.id)\
                 .order_by(func.count(models.quote_tag_association.c.quote_id).desc())\
                 .limit(10).all()
                 
    # 3. Sentiment Distribution
    sentiment_dist = db.query(models.Quote.sentiment_label, func.count(models.Quote.id).label('total'))\
                       .group_by(models.Quote.sentiment_label).all()

    return {
        "top_authors": [{"name": a[0], "count": a[1]} for a in top_authors],
        "top_tags": [{"name": a[0], "count": a[1]} for a in top_tags],
        "sentiment": [{"label": a[0], "count": a[1]} for a in sentiment_dist]
    }
