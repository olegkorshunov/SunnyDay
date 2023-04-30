from datetime import date

from fastapi import APIRouter

from src.hotel.dao import DaoHotel
from src.hotel.schemas import SHotelsWithAvail

router = APIRouter(
    prefix="/hotels",
    tags=["Hotel"],
)


@router.get("", response_model=list[SHotelsWithAvail])
async def get_hotels_with_available_rooms(location: str, date_from: date, date_to: date):
    result = await DaoHotel.get_hotels_with_available_rooms(location, date_from, date_to)
    return result
