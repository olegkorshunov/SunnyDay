from typing import TYPE_CHECKING

from sqlalchemy import JSON, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base

if TYPE_CHECKING:
    from src.hotel.room.models import Room


class Hotel(Base):
    __tablename__ = "hotel"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    location: Mapped[str] = mapped_column(String, nullable=False)
    services: Mapped[dict[str, list]] = mapped_column(JSON)
    rooms_quantity: Mapped[int] = mapped_column(Integer)
    image_id: Mapped[int] = mapped_column(Integer)
    room: Mapped[list["Room"]] = relationship(back_populates="hotel")

    def __repr__(self) -> str:
        return f"{self.name}"
