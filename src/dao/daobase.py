from typing import TYPE_CHECKING

from sqlalchemy import select

from src.database import async_session_maker

if TYPE_CHECKING:
    from src.database import Base


class BookingDaoBase:
    model: "Base" = None

    @classmethod
    async def get_all(cls):
        async with async_session_maker() as session:
            query = select(cls.model)
            result = await session.execute(query)
            return result.scalars().all()
