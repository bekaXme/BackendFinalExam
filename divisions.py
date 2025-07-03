from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

class Division(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    phone_number: int
    image_url: str
    
divisions : List[Division] = []
    
@router.get("/divisions", response_model=List[Division])
async def get_divisions():
    return divisions

@router.post("/divisions", response_model=Division)
async def add_division(new_division: Division):
    for div in divisions:
        if div.id == new_division.id:
            raise HTTPException(status_code=400, detail="Division with this ID already exists.")
    divisions.append(new_division)
    return new_division