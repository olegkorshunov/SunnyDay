from datetime import date

from sqlalchemy import func, select

from src.booking.models import Booking
from src.dao.daobase import DaoBase
from src.database import async_session_maker
from src.hotel.room.models import Room


class DaoRoom(DaoBase[Room]):
    model = Room

    @classmethod
    async def find_all(cls, hotel_id: int, date_from: date, date_to: date):
        """
        Find in hotel all not booked rooms.

        WITH hotel_rooms
            AS (SELECT *
                FROM   room
                WHERE  room.hotel_id = 5),
            booking_rooms
            AS (SELECT b.room_id                     AS room_id,
                        Coalesce(Count(b.room_id), 0) AS booking
                FROM   hotel_rooms AS hr
                        left join booking AS b
                            ON hr.id = b.room_id
                WHERE  hr.hotel_id = 5
                        AND ( '2024-08-15' <= date_from
                            AND date_from <= '2026-12-20' )
                        OR ( '2024-08-15' <= date_to
                            AND date_to <= '2026-12-20' )
                GROUP  BY b.room_id)
        SELECT hr.*,
            br.*,
            Date_part('day', '2024-08-15' :: timestamp - '2024-08-15' :: timestamp) *
            hr.price                              AS total_cost,
            Coalesce(hr.quantity - br.booking, 0) AS rooms_left
        FROM   hotel_rooms AS hr
            left join booking_rooms AS br
                    ON br.room_id = hr.id
        WHERE  hr.quantity - Coalesce(br.booking, 0) > 0
        """
        hotel_rooms = select(Room).where(Room.hotel_id == hotel_id).cte("hotel_rooms")
        booking_rooms = (
            select(Booking.room_id.label("room_id"), func.coalesce(func.count(Booking.room_id), 0).label("booking"))
            .join(hotel_rooms, hotel_rooms.c.id == Booking.id, isouter=True)
            .where(
                (hotel_rooms.c.hotel_id == hotel_id)
                & ((date_from <= Booking.date_from) & (Booking.date_from <= date_to))
                | (((date_from <= Booking.date_to) & (Booking.date_to <= date_to)))
            )
            .group_by(Booking.room_id)
        ).cte("booking_rooms")
        query = (
            select(
                hotel_rooms,
                booking_rooms,
                (func.Date_part("day", date_to - date_from) * hotel_rooms.c.price).label("total_cost"),
                (func.coalesce(hotel_rooms.c.quantity - booking_rooms.c.booking, 0)).label("rooms_left"),
            )
            .join(booking_rooms, booking_rooms.c.room_id == hotel_rooms.c.id, isouter=True)
            .where(hotel_rooms.c.quantity - func.coalesce(booking_rooms.c.booking, 0) > 0)
        )
        async with async_session_maker() as ssesion:
            result = await ssesion.execute(query)
            return result.mappings().all()
