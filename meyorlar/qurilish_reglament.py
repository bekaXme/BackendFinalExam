from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

# Ma'lumotlar modeli
class ConstructionRegulation(BaseModel):
    id: int
    title: str
    description: str
    url: str

db: List[ConstructionRegulation] = []

# 🔻 POST: Yangi reglamentsiya qo‘shish
@router.post("/qurilish_reglament", response_model=ConstructionRegulation)
async def create_regulation(item: ConstructionRegulation):
    if any(reg.id == item.id for reg in db):
        raise HTTPException(status_code=400, detail="Bu ID allaqachon mavjud.")
    db.append(item)
    return item

@router.get("/qurilish_reglament/{regulation_id}", response_model=ConstructionRegulation)
async def get_regulation(regulation_id: int):
    for reg in db:
        if reg.id == regulation_id:
            return reg
    raise HTTPException(status_code=404, detail="Ma'lumot topilmadi.")
