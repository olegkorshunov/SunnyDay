from datetime import date

from src.hotel.room.dao import DaoRoom
from src.hotel.router import router


@router.get("/{hotel_id}/rooms")
async def find_all(hotel_id: int, date_from: date, date_to: date):
    return await DaoRoom.find_all(hotel_id, date_from, date_to)
