from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def case_study_home():
    return {'msg': 'Case Study route'}
