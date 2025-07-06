from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

# Model: Yangilik
class NewsItem(BaseModel):
    id: int
    headline: str
    content: str
    published_at: str  # Misol: "2025-07-06"

# Vaqtinchalik baza
news_db: List[NewsItem] = []

# 🔻 POST: yangi yangilik qo‘shish
@router.post("/news", response_model=NewsItem)
async def create_news(item: NewsItem):
    if any(news.id == item.id for news in news_db):
        raise HTTPException(status_code=400, detail="Bu ID allaqachon mavjud.")
    news_db.append(item)
    return item

# 🔻 GET: ID orqali yangilik olish
@router.get("/news/{news_id}", response_model=NewsItem)
async def get_news(news_id: int):
    for news in news_db:
        if news.id == news_id:
            return news
    raise HTTPException(status_code=404, detail="Yangilik topilmadi.")
