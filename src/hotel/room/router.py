from datetime import date

from src.hotel.room.dao import DaoRoom
from src.hotel.room.schenas import SUnbookedRooms
from src.hotel.router import router


@router.get("/{hotel_id}/rooms", response_model=list[SUnbookedRooms])
async def find_all(hotel_id: int, date_from: date, date_to: date):
    result = await DaoRoom.find_all(hotel_id, date_from, date_to)
    return result
