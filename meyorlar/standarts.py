from fastapi import APIRouter
from pydantic import BaseModel



router = APIRouter()

class Standard(BaseModel):
    id: int
    title: str
    description: str
    
standards = []

@router.get('/standards', response_model=list[Standard])
async def get_standards():  
    return standards

@router.post('/standards', response_model=Standard)
async def create_standard(standard: Standard):
    for existing_standard in standards: 
        if existing_standard.id == standard.id:
            return {"message": "Standard with this ID already exists."}
    standards.append(standard)
    return standard