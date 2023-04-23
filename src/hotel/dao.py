from datetime import date

from src.dao.daobase import DaoBase
from src.hotel.models import Hotel


class DaoHotel(DaoBase):
    model = Hotel

    @classmethod
    async def get_hotels_with_available_rooms(cls, location: str, date_from: date, date_to: date):
        
        pass
