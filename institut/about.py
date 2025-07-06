# about_router.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

class AboutInfo(BaseModel):
    name: str
    description: str
    mission: str
    vision: str
    services: List[str]

about_data: Optional[AboutInfo] = None

@router.get("/about", response_model=AboutInfo)
async def get_about():
    if about_data is None:
        raise HTTPException(status_code=404, detail="About info not found.")
    return about_data

@router.post("/about", response_model=AboutInfo)
async def post_about_info(info: AboutInfo):
    global about_data
    about_data = info
    return about_data
