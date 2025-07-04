from fastapi import APIRouter

router = APIRouter()

@router.post("/burger-menu")
async def burger_menu():
    return {"message": "Burger menu endpoint called"}

@router.get("/burger-menu")
async def get_burger_menu():
    return {"message": "Burger menu retrieved successfully"}