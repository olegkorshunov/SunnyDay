from datetime import date

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


@router.get(path="", response_model=list[SBooking])
async def get(user: UserAccount = Depends(get_current_user)):
    return await BookingDao.find_all(user_account_id=user.id)


@router.post(path="", response_model=SBooking)
async def add(
    room_id: int,
    date_from: date,
    date_to: date,
    user: UserAccount = Depends(get_current_user),
):
    booking = await BookingDao.add(user.id, room_id, date_from, date_to)
    if not booking:
        raise HttpException.RoomCanNotBeBooked
    return booking


@router.delete(path="", response_model=SBooking | None)
async def delete(room_id: int, user: UserAccount = Depends(get_current_user)):
    return await BookingDao.delete(room_id=room_id, user_account_id=user.id)
