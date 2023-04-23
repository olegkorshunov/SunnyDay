from datetime import date

from src.hotel.router import router


@router.get("/{hotel_id}/rooms")
async def get_all_rooms(hotel_id: int, date_from: date, date_to: date):
    pass
