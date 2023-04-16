from src.booking.models import Booking
from src.dao.daobase import DaoBase


class BookingDao(DaoBase):
    model = Booking
