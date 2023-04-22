from pydantic import BaseModel, EmailStr


class SBaseUser(BaseModel):
    email: EmailStr

    class Config:
        orm_mode = True


class SUserLogin(SBaseUser):
    password: str


class SUserRegister(SBaseUser):
    id: int
    password: str


class SUserInfo(SBaseUser):
    id: int
