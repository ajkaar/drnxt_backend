# Entry point for FastAPI app
from fastapi import FastAPI
from app.routes import auth

app = FastAPI()
app.include_router(auth.router)

@app.get('/')
def read_root():
    return {"message": "Welcome to DRNXT API"}