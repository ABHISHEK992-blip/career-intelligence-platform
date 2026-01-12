from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from ..models import Domain
from .profile import async_session

DEFAULT_DOMAINS = [
    {"name": "Backend Developer", "description": "APIs, Databases, Server-side logic"},
    {"name": "Frontend Developer", "description": "UI, UX, Web interfaces"},
    {"name": "Full Stack Developer", "description": "Frontend + Backend"},
    {"name": "Data Science", "description": "Data analysis, ML, statistics"},
    {"name": "DevOps", "description": "CI/CD, Cloud, Infrastructure"}
]

async def seed_domains():
    async with async_session() as session:
        result = await session.execute(select(Domain))
        if result.scalars().first():
            return

        for domain in DEFAULT_DOMAINS:
            session.add(Domain(**domain))
        await session.commit()

async def get_all_domains():
    async with async_session() as session:
        result = await session.execute(select(Domain))
        return result.scalars().all()
