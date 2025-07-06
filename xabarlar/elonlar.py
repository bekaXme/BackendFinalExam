from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

# Model: E'lon
class Elon(BaseModel):
    id: int
    title: str
    body: str
    date: str  # Misol: "2025-07-06"

# Fake baza
elon_db: List[Elon] = []

# 🔻 POST: yangi e'lon qo‘shish
@router.post("/elon", response_model=Elon)
async def create_elon(item: Elon):
    if any(e.id == item.id for e in elon_db):
        raise HTTPException(status_code=400, detail="Bu ID allaqachon mavjud.")
    elon_db.append(item)
    return item

# 🔻 GET: ID orqali e'lonni olish
@router.get("/elon/{elon_id}", response_model=Elon)
async def get_elon(elon_id: int):
    for e in elon_db:
        if e.id == elon_id:
            return e
    raise HTTPException(status_code=404, detail="E'lon topilmadi.")
