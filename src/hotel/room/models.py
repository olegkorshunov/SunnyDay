from typing import TYPE_CHECKING

from sqlalchemy import JSON, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base

if TYPE_CHECKING:
    from src.booking.models import Booking
    from src.hotel.models import Hotel


class Room(Base):
    __tablename__ = "room"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=True)
    price: Mapped[int] = mapped_column(Integer)
    services: Mapped[dict[str, list]] = mapped_column(JSON)
    quantity: Mapped[int] = mapped_column(Integer)
    hotel_id: Mapped[int] = mapped_column(ForeignKey("hotel.id"))
    image_id: Mapped[int] = mapped_column(Integer)
    hotel: Mapped["Hotel"] = relationship(back_populates="room")
    booking: Mapped["Booking"] = relationship(back_populates="room")
