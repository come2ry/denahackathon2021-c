
from typing import Dict, Any
from core.config import settings
from sqlalchemy import create_engine  # type: ignore
from sqlalchemy.ext.declarative import declarative_base  # type: ignore
from sqlalchemy.orm import scoped_session, sessionmaker  # type: ignore
from config

engine = create_engine(
    config.DevelopmentConfig.SQLALCHEMY_DATABASE_URI,
    **config.DevelopmentConfig.SQLALCHEMY_ENGINE_OPTIONS
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()