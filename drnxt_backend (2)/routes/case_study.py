
from fastapi import APIRouter

case_study_router = APIRouter()

@case_study_router.get("/")
def get_case_studies():
    return {"case_studies": []}
