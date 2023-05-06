import asyncio
from datetime import date
from typing import Optional

from fastapi import APIRouter
from fastapi_cache.decorator import cache

from src.hotel.dao import DaoHotel
from src.hotel.schemas import SHotel, SHotelsWithRoomsLeft

router = APIRouter(
    prefix="/hotels",
    tags=["Hotel"],
)


@cache(expire=120)  # sec
@router.get("", response_model=list[SHotelsWithRoomsLeft])
async def get_hotels_by_location_and_time(location: str, date_from: date, date_to: date):
    # imatation of hight load
    await asyncio.sleep(5)  # sec
    result = await DaoHotel.find_all(location, date_from, date_to)
    return result


@router.get("id/{hotel_id}", response_model=Optional[SHotel])
async def get_hotel_by_id(hotel_id: int):
    return await DaoHotel.find_one_or_none(id=hotel_id)
