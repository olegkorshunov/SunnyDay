import uuid

from sqlalchemy import JSON, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from src.database import Base


class Room(Base):
    __tablename__ = "room"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    location: Mapped[str] = mapped_column(String, nullable=False)
    services: Mapped[dict[str, list]] = mapped_column(JSON)
    rooms_quantity: Mapped[int] = mapped_column(Integer)
    hotel_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("hotel.id"))
    image_id: Mapped[int] = mapped_column(Integer)
    hotel: Mapped["hotel"] = relationship("room")
    booking: Mapped["booking"] = relationship("room")
