from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

# Model
class Contact(BaseModel):
    id: int
    name: str
    phone: str
    address: str
    murojat: str

# Fake baza
contact_db: List[Contact] = []

# 🔻 POST: Foydalanuvchi murojaatini qabul qilish
@router.post("/contact", response_model=Contact)
async def create_contact(contact: Contact):
    if any(c.id == contact.id for c in contact_db):
        raise HTTPException(status_code=400, detail="Bu ID allaqachon mavjud.")
    contact_db.append(contact)
    return contact

# 🔻 GET: ID orqali murojaatni olish
@router.get("/contact/{contact_id}", response_model=Contact)
async def get_contact(contact_id: int):
    for c in contact_db:
        if c.id == contact_id:
            return c
    raise HTTPException(status_code=404, detail="Murojaat topilmadi.")
