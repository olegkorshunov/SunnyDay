from src.booking.models import Booking
from src.dao.daobase import BookingDaoBase


class BookingDao(BookingDaoBase):
    model = Booking
