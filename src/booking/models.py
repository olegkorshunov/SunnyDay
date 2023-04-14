from datetime import date

from sqlalchemy import Computed, Date, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base


class Booking(Base):
    __tablename__ = "booking"
    id: Mapped[int] = mapped_column(primary_key=True)
    room_id: Mapped[int] = mapped_column(ForeignKey("room.id"))
    user_account_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    date_from: Mapped[date] = mapped_column(Date)
    date_to: Mapped[date] = mapped_column(Date)
    price: Mapped[int] = mapped_column(Integer)
    total_cost: Mapped[int] = mapped_column(Integer, Computed("(date_from - date_to) * price"))
    total_days: Mapped[int] = mapped_column(Integer, Computed("date_from - date_to"))
    room: Mapped["room"] = relationship(back_populates="booking")
    user_account: Mapped["user_account"] = relationship(back_populates="booking")
