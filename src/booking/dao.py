from datetime import date
from typing import Optional

from sqlalchemy import func, insert, select

from src.booking.models import Booking
from src.dao.daobase import DaoBase
from src.database import async_session_maker
from src.hotel.room.models import Room


class BookingDao(DaoBase[Booking]):
    model = Booking

    @classmethod
    async def add(cls, user_id: int, room_id: int, date_from: date, date_to: date) -> Optional[Booking]:
        """
        example:
        -- date_from = '2023-05-15'
        -- date_to   = '2023-06-20'
        -- room_id   = 1
        WITH booked_room
            AS (SELECT *
                FROM   booking
                WHERE  room_id = 1
                        AND ( '2023-05-15' <= date_from
                            AND date_from <= '2023-06-20' )
                        OR ( '2023-05-15' <= date_to
                            AND date_to <= '2023-06-20' ))
        SELECT room.quantity - Count(booked_room.room_id)
        FROM   room
            LEFT JOIN booked_room
                    ON booked_room.room_id = room.id
        WHERE  room.id = 1
        GROUP  BY room.quantity,
                booked_room.room_id

        """

        booked_room_query = (
            select(Booking)
            .where(
                (Booking.room_id == room_id)
                & (
                    (date_from <= Booking.date_from) & (date_from <= Booking.date_to)
                    | ((date_to <= Booking.date_from) & (date_to <= Booking.date_to))
                )
            )
            .cte("booked_room")
        )
        # counting numbers of free rooms
        room_query = (
            select(Room.quantity - func.count(booked_room_query.c.room_id).label("room_left"))
            .select_from(Room)
            .join(booked_room_query, booked_room_query.c.room_id == Room.id, isouter=True)
            .where(Room.id == room_id)
        ).group_by(Room.quantity, booked_room_query.c.room_id)

        async with async_session_maker() as sessesion:
            room_is_free: int | None = await sessesion.scalar(room_query)
            print(room_is_free)
            if room_is_free:
                get_price = select(Room.price).filter_by(id=room_id)
                price: int | None = await sessesion.scalar(get_price)
                add_booking_stmt = (
                    insert(Booking)
                    .values(
                        room_id=room_id,
                        user_account_id=user_id,
                        date_from=date_from,
                        date_to=date_to,
                        price=price,
                    )
                    .returning(Booking)
                )
                new_booking = await sessesion.scalar(add_booking_stmt)
                await sessesion.commit()
                return new_booking
