from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import MetaData, Integer, String, TIMESTAMP, ForeignKey, Column, JSON, Table, Boolean

import os
from dotenv import load_dotenv
import datetime

from models.models import UsersPermissions
load_dotenv()

DATABASE_URL = "postgresql+asyncpg://postgres:123123@localhost:5432/postgres"

class Base(DeclarativeBase):
    pass    


class User(SQLAlchemyBaseUserTable[int], Base):

    id = Column(Integer, primary_key=True),
    name = Column(String, nullable=False),
    register_time = Column(TIMESTAMP, default=datetime.datetime.now(datetime.UTC)),
    permissions = Column(Integer, ForeignKey(UsersPermissions.c.id))

    email = Column(
            String(length=320), unique=True, index=True, nullable=False
        )
    hashed_password = Column(
        String(length=1024), nullable=False
    )
    is_active =  Column(Boolean, default=True, nullable=False)
    is_superuser = Column(
        Boolean, default=False, nullable=False
    )
    is_verified = Column(
        Boolean, default=False, nullable=False
    )


engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
