from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

class Vacancy(BaseModel):
    id: int
    title: str
    description: str
    requirements: List[str]
    salary: float
    image_url: str
    
vacancies: List[Vacancy] = []

@router.get("/vacancies", response_model=List[Vacancy])
async def get_vacancies():
    return vacancies

@router.post("/vacancies", response_model=Vacancy)
async def add_vacancy(new_vacancy: Vacancy):
    for vac in vacancies:
        if vac.id == new_vacancy.id:
            raise HTTPException(status_code=400, detail="Vacancy with this ID already exists.")
    vacancies.append(new_vacancy)
    return new_vacancy