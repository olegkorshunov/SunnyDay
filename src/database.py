from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy_utils import create_database, database_exists, drop_database

from src.config import settings

import src.exceptions as ex


class Base(DeclarativeBase):
    pass


engine = create_async_engine(settings.DATABASE_URL_ASYNC)
async_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

if settings.MODE == "TEST":
    if database_exists(settings.DATABASE_URL_SYNC):
        raise ex.DBAlredyExist("Test")
else:
    create_database(settings.DATABASE_URL_SYNC)


async def insert_data():
    global async_session_maker
    async with async_session_maker() as session:
        query = text(
            """
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema='public' AND table_type='BASE TABLE'
            """
        )
        tables = await session.execute(query)
        if len(tables.all()) > 1:
            query = text(
                """
            SELECT * from user_account
            """
            )
        users = await session.execute(query)
        if len(users.all()) == 0:
            with open("db_data/insert_data.sql") as sql_file:
                for statement in sql_file.read().split(";"):
                    if len(statement.strip()) > 0:
                        await session.execute(text(statement + ";"))
                        await session.commit()
