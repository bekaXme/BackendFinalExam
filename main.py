# main.py

from fastapi import FastAPI
from institut.registration import router
from menu import router as menu_router
from institut.about import router as about_router
from institut.management import router as management_router
from institut.structer import router as structure_router
from institut.divisions import router as divisions_router
from institut.vacansiyalar import router as vacansiyalar_router
from menu_options import router as menu_options_router
from meyorlar.laws import router as laws_router
from submenu import router as submenu_router
from meyorlar.shnq import router as shnq_router
from meyorlar.reference import router as reference_router
from meyorlar.standarts import router as standards_router
from meyorlar.qurilish_reglament import router as qurilish_reglament_router
from xabarlar.corrupsiya import router as corrupsiya_router
from xabarlar.elonlar import router as elonlar_router
from xabarlar.news import router as news_router
from contacts.contact import router as contact_router

app = FastAPI(title="AuthX + FastAPI Example")

# Include the router
app.include_router(router, prefix="/auth", tags=["Auth"])
app.include_router(menu_router, tags=["Menu"])
app.include_router(about_router, tags=["About"])
app.include_router(management_router, tags=["Management"])
app.include_router(structure_router, tags=["Structure"])
app.include_router(divisions_router, tags=["Divisions"])
app.include_router(vacansiyalar_router, tags=["Vacansiyalar"])
app.include_router(menu_options_router, tags=["Menu Options"])
app.include_router(laws_router, tags=["Laws"])
app.include_router(submenu_router, tags=["Submenu"])
app.include_router(shnq_router, tags=["SHNQ"])
app.include_router(reference_router, tags=["Reference"])
app.include_router(standards_router, tags=["Standards"])
app.include_router(qurilish_reglament_router, tags=["Qurilish Reglament"])
app.include_router(corrupsiya_router, tags=["Corrupsiya"])
app.include_router(elonlar_router, tags=["Elonlar"])
app.include_router(news_router, tags=["News"])
app.include_router(contact_router, tags=["Contact"])

@app.get("/")
async def root():
    return {"message": "Welcome to the AuthX + FastAPI Example!"}
