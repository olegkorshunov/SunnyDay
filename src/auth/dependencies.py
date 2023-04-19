from datetime import datetime

from fastapi import Depends, HTTPException, Request, status
from jose import JWTError, jwt

from src.auth.dao import DaoAuth
from src.config import settings
from src.auth.constants import access_token


def get_access_token(request: Request):
    access_token_jwt = request.cookies.get(access_token)
    if not access_token_jwt:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return access_token_jwt


async def get_current_user(access_token_jwt: str = Depends(get_access_token)):
    try:
        payload = jwt.decode(access_token_jwt, settings.SECRET_KEY_jwt, algorithms=settings.ALGORITHM)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    expire = payload.get("exp")
    if not expire or int(expire) < datetime.utcnow().timestamp():
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    user = await DaoAuth.find_one_by_id(int(user_id))
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return user
