import uvicorn
from fastapi import FastAPI
from fastapi_users import FastAPIUsers

import src.models  # noqa
from src.auth.auth import auth_backend
from src.auth.models import UserAccount
from src.auth.schemas import UserCreate, UserRead
from src.auth.usermanager import get_user_manager
from src.booking.router import router as booking_router

app = FastAPI()

fastapi_users = FastAPIUsers[UserAccount, int](
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


app.include_router(booking_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
