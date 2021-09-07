import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from core.config import settings


SQLALCHEMY_DATABASE_URL=settings.DATABASE_URL

engine=create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal=sessionmaker(bind=engine,autocommit=False,autoflush=False)