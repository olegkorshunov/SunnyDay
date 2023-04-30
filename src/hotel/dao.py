from datetime import date

from sqlalchemy import func, select, text

from src.dao.daobase import DaoBase
from src.database import async_session_maker
from src.hotel.models import Hotel

from ..booking.models import Booking
from .room.models import Room


class DaoHotel(DaoBase[Hotel]):
    model = Hotel

    @classmethod
    async def get_hotels_with_available_rooms(cls, location: str, date_from: date, date_to: date):
        """
        WITH hotel_by_location
            AS (SELECT *
                FROM   hotel
                WHERE  Lower(location) LIKE '%al%'),
            number_of_boocked_room
            AS (SELECT r.hotel_id      AS hotel_id,
                        Count(hotel_id) AS number_of_boocked_room
                FROM   booking AS b
                        LEFT JOIN room AS r
                            ON b.room_id = r.id
                WHERE  ( '2023-05-15' <= date_from
                        AND date_from <= '2023-06-20' )
                        OR ( '2023-05-15' <= date_to
                            AND date_to <= '2023-06-20' )
                GROUP  BY r.hotel_id)
        SELECT h.*,
            ( h.rooms_quantity - COALESCE(n.number_of_boocked_room, 0) ) AS room_left
        FROM   hotel_by_location AS h
            LEFT JOIN number_of_boocked_room AS n
                    ON h.id = n.hotel_id
        WHERE  h.rooms_quantity - COALESCE(n.number_of_boocked_room, 0) > 0
        """
        h = select(Hotel).where(func.lower(Hotel.location).like(f"%{location}%")).cte("hotel_by_location")
        n = (
            (
                select(Room.hotel_id.label("hotel_id"), func.count(Room.hotel_id).label("number_of_boocked_room"))
                .outerjoin(Booking, Booking.room_id == Room.id)
                .where(
                    ((date_from <= Booking.date_from) & (Booking.date_from <= date_to))
                    | (((date_from <= Booking.date_to) & (Booking.date_to <= date_to)))
                )
            )
            .group_by(Room.hotel_id)
            .cte("number_of_boocked_room")
        )

        hotels_with_available_rooms = (
            select(h, (h.c.rooms_quantity - func.coalesce(n.c.number_of_boocked_room, 0)).label("rooms_left"))
            .outerjoin(n, h.c.id == n.c.hotel_id)
            .where((h.c.rooms_quantity - func.coalesce(n.c.number_of_boocked_room, 0) > 0))
        )
        async with async_session_maker() as ssesion:
            hotels_with_available_rooms = await ssesion.execute(hotels_with_available_rooms)
            result = hotels_with_available_rooms.mappings().all()
            return result
