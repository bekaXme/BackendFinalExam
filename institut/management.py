# management_router.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

class Manager(BaseModel):
    id: int
    full_name: str
    position: str
    image_url: str
    bio: Optional[str] = None

managers: List[Manager] = []

@router.get("/management", response_model=List[Manager])
async def get_management():
    return managers

@router.post("/management", response_model=Manager)
async def add_manager(manager: Manager):
    for m in managers:
        if m.id == manager.id:
            raise HTTPException(status_code=400, detail="Manager with this ID already exists.")
    managers.append(manager)
    return manager
