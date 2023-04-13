import uuid
from datetime import date

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from sqlalchemy import Computed, Date, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base


class Booking(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "booking"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    room_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("room.id"))
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("user.id"))
    date_from: Mapped[date] = mapped_column(Date)
    date_to: Mapped[date] = mapped_column(Date)
    price: Mapped[int] = mapped_column(Integer)
    total_cost: Mapped[int] = mapped_column(Integer, Computed("(date_from - date_to) * price"))
    total_days: Mapped[int] = mapped_column(Integer, Computed("date_from - date_to"))
    room: Mapped["room"] = relationship("booking")
    user: Mapped["user"] = relationship("booking")
