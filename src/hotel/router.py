from datetime import date

from fastapi import APIRouter

from src.hotel.dao import DaoHotel

router = APIRouter(
    prefix="/hotels",
    tags=["Hotel"],
)


@router.get("")
async def get_hotels_with_available_rooms(location: str, date_from: date = None, date_to: date = None):
    return await DaoHotel.get_hotels_with_available_rooms(location, date_from, date_to)
