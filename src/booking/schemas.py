from datetime import date

from pydantic import BaseModel


class SBooking(BaseModel):
    id: int
    room_id: int
    user_account_id: int
    date_from: date
    date_to: date
    price: int
    total_cost: int
    total_days: int
    room: int
    user_account: int

    class Config:
        orm_mode = True
