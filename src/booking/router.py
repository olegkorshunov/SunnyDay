from datetime import date
from typing import List

from fastapi import APIRouter, Depends

from src.auth.dependencies import get_current_user
from src.auth.models import UserAccount
from src.booking.dao import BookingDao
from src.booking.schemas import SBooking
from src.exceptions import HttpException

router = APIRouter(
    prefix="/boockings",
    tags=["Bookings"],
)


@router.get("/")
async def get(user: UserAccount = Depends(get_current_user)) -> List[SBooking]:
    return await BookingDao.find_all(id=user.id)  # type: ignore


@router.post("/")
async def add(
    room_id: int,
    date_from: date,
    date_to: date,
    user: UserAccount = Depends(get_current_user),
):
    booking = await BookingDao.add(user.id, room_id, date_from, date_to)
    if not booking:
        raise HttpException.RoomCanNotBeBooked
