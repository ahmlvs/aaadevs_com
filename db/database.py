import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Ensure the `db/` directory exists
os.makedirs("db", exist_ok=True)

DATABASE_URL = "sqlite+aiosqlite:///./db/test.db"  # Async SQLite database

# Create the async database engine
async_engine = create_async_engine(DATABASE_URL, echo=True)

# Create an async session maker
AsyncSessionLocal = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    autocommit=False,
    autoflush=False,
)

# Base class for models
Base = declarative_base()

# Dependency to get the database session
async def get_db_session():
    async with AsyncSessionLocal() as session:
        yield session
