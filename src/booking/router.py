from datetime import date

from fastapi import APIRouter, Depends

from src.auth.dependencies import get_current_user
from src.auth.models import UserAccount
from src.booking.dao import DaoBooking
from src.booking.schemas import SBooking, SBookingWithImage
from src.exceptions import HttpException

router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"],
)


@router.get(path="", response_model=list[SBookingWithImage])
async def get_bookings(user: UserAccount = Depends(get_current_user)):
    res = await DaoBooking.get_booking_with_image(user_account_id=user.id)
    return res


@router.post(path="", response_model=SBooking)
async def add_booking(
    room_id: int,
    date_from: date,
    date_to: date,
    user: UserAccount = Depends(get_current_user),
):
    booking = await DaoBooking.add(user.id, room_id, date_from, date_to)
    if not booking:
        raise HttpException.RoomCanNotBeBooked
    return booking


@router.delete(path="", response_model=SBooking | None)
async def delete_booking_by_id(booking_id: int, user: UserAccount = Depends(get_current_user)):
    await DaoBooking.delete_booking_by_id(booking_id=booking_id, user_account_id=user.id)
