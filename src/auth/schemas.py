from pydantic import BaseModel, EmailStr


class SUserRegister(BaseModel):
    id: int
    email: EmailStr
    password: str


class SUserAuth(BaseModel):
    email: EmailStr
    password: str
