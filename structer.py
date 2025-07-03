# structure_router.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

class StructureImage(BaseModel):
    image_url: str

structure_data: Optional[StructureImage] = None

@router.get("/structure", response_model=StructureImage)
async def get_structure():
    if not structure_data:
        raise HTTPException(status_code=404, detail="Structure image not found.")
    return structure_data

@router.post("/structure", response_model=StructureImage)
async def post_structure(data: StructureImage):
    global structure_data
    structure_data = data
    return structure_data
