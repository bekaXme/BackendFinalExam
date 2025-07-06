from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

# Model: Ma'lumotnoma
class Reference(BaseModel):
    id: int
    title: str
    content: str
    source_url: str

reference_db: List[Reference] = []

@router.post("/reference", response_model=Reference)
async def create_reference(item: Reference):
    if any(ref.id == item.id for ref in reference_db):
        raise HTTPException(status_code=400, detail="Bu ID allaqachon mavjud.")
    reference_db.append(item)
    return item

@router.get("/reference/{reference_id}", response_model=Reference)
async def get_reference(reference_id: int):
    for ref in reference_db:
        if ref.id == reference_id:
            return ref
    raise HTTPException(status_code=404, detail="Ma'lumotnoma topilmadi.")
