from datetime import date
from typing import Optional

from fastapi import APIRouter

from src.hotel.dao import DaoHotel
from src.hotel.schemas import Shotel, SHotelsWithRoomsLeft

router = APIRouter(
    prefix="/hotels",
    tags=["Hotel"],
)


@router.get("", response_model=list[SHotelsWithRoomsLeft])
async def find_all(location: str, date_from: date, date_to: date):
    result = await DaoHotel.find_all(location, date_from, date_to)
    return result


@router.get("id/{hotel_id}", response_model=Optional[Shotel])
async def get_hotel_by_id(hotel_id: int):
    return await DaoHotel.find_one_or_none(id=hotel_id)
