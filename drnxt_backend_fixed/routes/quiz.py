from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def quiz_home():
    return {'msg': 'Quiz route'}
