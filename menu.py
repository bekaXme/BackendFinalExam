# menu_router.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

# Fake in-memory menu list (can be replaced with DB)
menu_items = []

class MenuItem(BaseModel):
    id: int
    name: str
    description: str
    image_url: str


@router.get("/menu", response_model=List[MenuItem])
async def get_menu():
    return menu_items


@router.post("/post_menu_item", response_model=MenuItem)
async def post_menu_item(item: MenuItem):
    for existing_item in menu_items:
        if existing_item.id == item.id:
            raise HTTPException(status_code=400, detail="Menu item with this ID already exists.")
    
    menu_items.append(item)
    return item
