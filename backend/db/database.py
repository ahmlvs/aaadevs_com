import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from config import PROFILES, DB_URL
import ssl

# Determine the database URL based on the environment
if PROFILES == "prod":

    # PostgreSQL Production Database URL
    # "postgresql+asyncpg://user:password@localhost/prod_db"

    # MySQL Production Database URL
    # "mysql+aiomysql://user:password@localhost/prod_db"

    DATABASE_URL = DB_URL

    ssl_args = {
        # 'ssl': True,
        "ssl": ssl._create_unverified_context()
    }

    # Create an asynchronous engine
    async_engine = create_async_engine(DATABASE_URL, connect_args = ssl_args, echo=False)
else:
    # Ensure the `db/` directory exists
    os.makedirs("db", exist_ok=True)
    # Async SQLite database
    DATABASE_URL = "sqlite+aiosqlite:///./db/test.db"

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
