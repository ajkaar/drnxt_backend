
from fastapi import APIRouter

quiz_router = APIRouter()

@quiz_router.get("/")
def get_quizzes():
    return {"quizzes": []}
