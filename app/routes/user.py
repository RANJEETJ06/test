from fastapi import APIRouter
from app.services.user_service import get_users

router = APIRouter()

@router.get("/users")
def users():
    return get_users()