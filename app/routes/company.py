# app/routes/company.py

from fastapi import APIRouter

router = APIRouter(prefix="/company", tags=["Company"])

@router.get("/")
def get_companies():
    return {"message": "Company route working"}