from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Dict

router = APIRouter()

class SubmenuItem(BaseModel):
    id: int
    title: str
    url: str
    icon: str
    
submenues : List[SubmenuItem] = []

@router.get('/submenu', response_model=List[SubmenuItem])
async def get_submenu():
    return submenues

@router.post('/submenu', response_model=SubmenuItem)
async def create_submenu(submenu: dict):
    for menu in submenues:
        if menu.id == submenu['id']:
            return {"message": "Submenu with this ID already exists."}
        else :
            submenues.append(SubmenuItem(**submenu))
            return submenu