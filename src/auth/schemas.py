from pydantic import BaseModel, EmailStr


class SUserRegister(BaseModel):
    id: int
    email: EmailStr
    password: str
