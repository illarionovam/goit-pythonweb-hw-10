from fastapi import APIRouter, Depends
from src.schemas import UserResponse
from src.services.auth import get_current_user

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me", response_model=UserResponse)
async def me(user: UserResponse = Depends(get_current_user)):
    return user
