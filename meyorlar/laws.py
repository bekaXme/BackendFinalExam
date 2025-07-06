from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Dict

router = APIRouter()

class Law(BaseModel):
    id: int
    title: str
    description: str
    
laws: List[Law] = []
@router.get('/laws', response_model=List[Law])
async def get_laws():
    return laws

@router.post('/laws', response_model=Law)
async def create_law(law: Law):
    for existing_law in laws:
        if existing_law.id == law.id:
            return {"message": "Law with this ID already exists."}      
    laws.append(law)
    return law