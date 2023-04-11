import uuid

from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from src.auth.auth import auth_backend
from src.auth.models import User
from src.auth.schemas import UserCreate, UserRead
from src.auth.usermanager import get_user_manager

app = FastAPI()

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
