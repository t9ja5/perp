from fastapi import FastAPI
from app.db.session import engine
from app.db.base import Base
from app.models import student  # important import
from app.routes.student import router as student_router
from app.routes.company import router as company_router
from app.routes.placement_coordinator import router as placement_router

app = FastAPI()

app.include_router(student_router)
app.include_router(company_router)
app.include_router(placement_router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "Welcome to PERP Backend 🚀"}