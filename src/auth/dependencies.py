from datetime import datetime

from fastapi import Depends, Request
from jose import JWTError, jwt

import src.exceptions as ex
from src.auth.constants import access_token
from src.auth.dao import DaoAuth
from src.config import settings


def get_access_token(request: Request):
    access_token_jwt = request.cookies.get(access_token)
    if not access_token_jwt:
        raise ex.TokenAbsent
    return access_token_jwt


async def get_current_user(access_token_jwt: str = Depends(get_access_token)):
    try:
        payload = jwt.decode(access_token_jwt, settings.SECRET_KEY_jwt, algorithms=settings.ALGORITHM)
    except JWTError:
        raise ex.IncorrectTokenFormat
    expire = payload.get("exp")
    if not expire or int(expire) < datetime.utcnow().timestamp():
        raise ex.AuthTokenExpire
    user_id = payload.get("sub")
    if not user_id:
        raise ex.UserDataNotFound
    user = await DaoAuth.find_one_by_id(int(user_id))
    if not user:
        raise exс.UserDataNotFound
    return user
