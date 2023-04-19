from datetime import datetime, timedelta

from fastapi import HTTPException
from jose import jwt
from passlib.context import CryptContext
from pydantic import EmailStr

from src.auth.dao import DaoAuth
from src.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(hours=3)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY_jwt, algorithm=settings.ALGORITHM)
    return encoded_jwt


async def authenticate_user(email: EmailStr, password: str):
    user = await DaoAuth.find_one_or_none(email=email)
    if not (user and verify_password(password, user.hashed_password)):
        raise HTTPException(status_code=500)
    return user
