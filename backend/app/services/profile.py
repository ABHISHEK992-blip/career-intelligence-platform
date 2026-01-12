from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.future import select

from ..models import Base, User
from ..schemas import UserCreate, UserUpdate

DATABASE_URL = "sqlite+aiosqlite:///./career_intelligence.db"

# Async Engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Async Session
async_session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)

# Initialize Database
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# -------------------- CRUD OPERATIONS --------------------

# Create User
async def create_user(user: UserCreate):
    async with async_session() as session:
        db_user = User(**user.dict())
        session.add(db_user)
        await session.commit()
        await session.refresh(db_user)
        return db_user

# Get User by ID
async def get_user(user_id: int):
    async with async_session() as session:
        result = await session.execute(
            select(User).where(User.id == user_id)
        )
        return result.scalar_one_or_none()

# Update User
async def update_user(user_id: int, user_update: UserUpdate):
    async with async_session() as session:
        result = await session.execute(
            select(User).where(User.id == user_id)
        )
        db_user = result.scalar_one_or_none()

        if not db_user:
            return None

        for key, value in user_update.dict(exclude_unset=True).items():
            setattr(db_user, key, value)

        await session.commit()
        await session.refresh(db_user)
        return db_user

# Delete User
async def delete_user(user_id: int):
    async with async_session() as session:
        result = await session.execute(
            select(User).where(User.id == user_id)
        )
        db_user = result.scalar_one_or_none()

        if not db_user:
            return None

        await session.delete(db_user)
        await session.commit()
        return db_user
