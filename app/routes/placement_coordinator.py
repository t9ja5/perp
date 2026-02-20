# app/routes/placement_coordinator.py

from fastapi import APIRouter

router = APIRouter(prefix="/placement_coordinator", tags=["Placement_Coordinator"])

@router.get("/")
def get_companies():
    return {"message": "Placement Coordinator route working"}