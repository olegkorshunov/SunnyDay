from typing import List

from fastapi import APIRouter, Depends

from src.auth.dependencies import get_current_user
from src.auth.models import UserAccount
from src.booking.dao import BookingDao
from src.booking.schemas import SBooking

router = APIRouter(
    prefix="/boocking",
    tags=["Booking"],
)


@router.get("/")
async def get(user: UserAccount = Depends(get_current_user)) -> List[SBooking]:
    return await BookingDao.find_all(id=user.id)  # type: ignore
