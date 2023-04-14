from typing import List

from fastapi import APIRouter

from src.booking.dao import BookingDao
from src.booking.schemas import SBooking

router = APIRouter(
    prefix="/boocking",
    tags=["Booking"],
)


@router.get("/")
async def get() -> List[SBooking]:
    return await BookingDao.get_all()
