from fastapi import APIRouter, Query, HTTPException
from pydantic import BaseModel
from typing import List, Dict

router = APIRouter()

stored_menu: Dict[str, Dict] = {}

# Define models for input
class MenuLang(BaseModel):
    title: str
    items: List[str]

class BurgerMenu(BaseModel):
    uz: MenuLang
    en: MenuLang
    ru: MenuLang

@router.post("/burger-menu")
async def post_burger_menu(menu: BurgerMenu):
    global stored_menu
    stored_menu = {
        "uz": menu.uz.dict(),
        "en": menu.en.dict(),
        "ru": menu.ru.dict(),
    }
    return {"message": "Burger menu saved successfully"}

@router.get("/burger-menu")
async def get_burger_menu(lang: str = Query("uz", enum=["uz", "en", "ru"])):
    if lang not in stored_menu:
        raise HTTPException(status_code=404, detail="Menu not found for this language")
    return stored_menu[lang]
