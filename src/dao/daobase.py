from typing import Generic, Optional, Sequence, Type, TypeVar

from sqlalchemy import delete, insert, select

from src.database import Base, async_session_maker

ModelType = TypeVar("ModelType", bound=Base)


class DaoBase(Generic[ModelType]):
    model: Type[ModelType]

    @classmethod
    async def find_one_by_id(cls, model_id: int) -> Optional[ModelType]:
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=model_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_one_or_none(cls, **filter_by) -> Optional[ModelType]:
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_all(cls, **filter_by) -> Sequence[ModelType]:
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.scalars(query)
            return result.all()

    @classmethod
    async def insert(cls, **data) -> Optional[ModelType]:
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data).returning(cls.model)
            result = await session.scalar(query)
            await session.commit()
            return result

    @classmethod
    async def delete(cls, **filter_by) -> Optional[ModelType]:
        async with async_session_maker() as session:
            stmt = delete(cls.model).filter_by(**filter_by).returning(cls.model)
            result = await session.scalar(stmt)
            await session.commit()
            return result
