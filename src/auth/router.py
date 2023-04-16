from fastapi import APIRouter, HTTPException

from src.auth.auth import get_password_hash
from src.auth.dao import DaoAuth
from src.auth.schemas import SUserRegister

router = APIRouter(
    prefix="/auth",
    tags=["Auth & Users"],
)


@router.post("/register")
async def register_user(user_data: SUserRegister):
    existig_user = await DaoAuth.find_one_or_none(email=user_data.email)
    if existig_user:
        raise HTTPException(status_code=500)
    hashed_password = get_password_hash(password=user_data.password)
    await DaoAuth.insert(email=user_data.email, hashed_password=hashed_password)