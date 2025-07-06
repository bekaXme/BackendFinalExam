from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import HTMLResponse

router = APIRouter()

class shnq(BaseModel):
    id : int
    title: str
    description: str
    url: str
    
shnqs = []

@router.get('/shnq', response_model=list[shnq])
async def get_shnq():
    return shnqs

@router.post('/shnq', response_model=shnq)
async def create_shnq(shnq: shnq):
    for existing_shnq in shnqs: 
        if existing_shnq.id == shnq.id:
            return {"message": "SHNQ with this ID already exists."}
    shnqs.append(shnq)  
    return shnq
