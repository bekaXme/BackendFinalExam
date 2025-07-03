# main.py

from fastapi import FastAPI
from registration import router
from menu import router as menu_router
from about import router as about_router
from management import router as management_router
from structer import router as structure_router
from divisions import router as divisions_router
from vacansiyalar import router as vacansiyalar_router


app = FastAPI(title="AuthX + FastAPI Example")

# Include the router
app.include_router(router, prefix="/auth", tags=["Auth"])
app.include_router(menu_router, tags=["Menu"])
app.include_router(about_router, tags=["About"])
app.include_router(management_router, tags=["Management"])
app.include_router(structure_router, tags=["Structure"])
app.include_router(divisions_router, tags=["Divisions"])
app.include_router(vacansiyalar_router, tags=["Vacansiyalar"])

@app.get("/")
async def root():
    return {"message": "Welcome to the AuthX + FastAPI Example!"}
