
from fastapi import FastAPI
from routes.auth import auth_router
from routes.quiz import quiz_router
from routes.case_study import case_study_router

app = FastAPI()

app.include_router(auth_router, prefix="/auth")
app.include_router(quiz_router, prefix="/quiz")
app.include_router(case_study_router, prefix="/case")
