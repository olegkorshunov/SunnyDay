from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base

if TYPE_CHECKING:
    from src.booking.models import Booking


class UserAccount(Base):
    __tablename__ = "user_account"
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    booking: Mapped[list["Booking"]] = relationship(back_populates="user_account")

    # TODO: add roles: [user,admin] for admin panel, and in the future comments and stars

    def __repr__(self) -> str:
        return f"{self.email}"
