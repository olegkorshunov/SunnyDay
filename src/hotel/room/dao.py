from datetime import date
from src.hotel.room.models import Room
from src.dao.daobase import DaoBase


class DaoRoom(DaoBase[Room]):
    model = Room

    @classmethod
    def get_hotel_rooms(cls, hotel_id: int, date_from: date, date_to: date):
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
        pass
