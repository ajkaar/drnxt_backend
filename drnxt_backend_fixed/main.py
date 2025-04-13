from fastapi import FastAPI
from routes import auth, quiz, case_study

app = FastAPI()

app.include_router(auth.router, prefix="/auth")
app.include_router(quiz.router, prefix="/quiz")
app.include_router(case_study.router, prefix="/case")
