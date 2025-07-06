from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List
import shutil
import os

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

class AnticorruptionPost(BaseModel):
    id: int
    title: str
    description: str
    filename: str

db: List[AnticorruptionPost] = []

# 🔻 POST: fayl + title + description
@router.post("/anticorruption", response_model=AnticorruptionPost)
async def upload_anticorruption(
    id: int = Form(...),
    title: str = Form(...),
    description: str = Form(...),
    file: UploadFile = File(...)
):
    if any(item.id == id for item in db):
        raise HTTPException(status_code=400, detail="Bu ID allaqachon mavjud.")

    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    new_item = AnticorruptionPost(
        id=id,
        title=title,
        description=description,
        filename=file.filename
    )
    db.append(new_item)
    return new_item

# 🔻 GET: ID orqali ma'lumot
@router.get("/anticorruption/{item_id}", response_model=AnticorruptionPost)
async def get_anticorruption(item_id: int):
    for item in db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Topilmadi")

# 🔻 GET: Faylni ko‘rsatish
@router.get("/anticorruption/file/{filename}")
async def get_uploaded_file(filename: str):
    file_path = os.path.join(UPLOAD_DIR, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Fayl topilmadi")
    return FileResponse(file_path)
