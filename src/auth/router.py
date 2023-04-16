from fastapi import APIRouter, HTTPException, Response

from src.auth.auth import authenticate_user, create_access_token, get_password_hash
from src.auth.dao import DaoAuth
from src.auth.schemas import SUserAuth, SUserRegister

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


@router.post("/login")
async def login_user(response: Response, user_data: SUserAuth):
    user: SUserRegister = await authenticate_user(user_data.email, user_data.password)
    access_token = create_access_token({"sub": user.id})
    response.set_cookie("booking_access_token", access_token)
    return access_token
