from fastapi import APIRouter

router = APIRouter()

@router.post("/burger-menu")
async def 