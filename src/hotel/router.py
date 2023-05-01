from datetime import date

from fastapi import APIRouter

from src.hotel.dao import DaoHotel
from src.hotel.schemas import SHotelsWithRoomsLeft

router = APIRouter(
    prefix="/hotels",
    tags=["Hotel"],
)


@router.get("", response_model=list[SHotelsWithRoomsLeft])
async def find_all(location: str, date_from: date, date_to: date):
    result = await DaoHotel.find_all(location, date_from, date_to)
    return result
