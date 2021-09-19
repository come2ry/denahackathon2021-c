from flask_sqlalchemy import SQLAlchemy
from typing import Dict, Any
from sqlalchemy import create_engine  # type: ignore
from sqlalchemy.ext.declarative import declarative_base  # type: ignore
from sqlalchemy.orm import scoped_session, sessionmaker  # type: ignore

import config

db = SQLAlchemy()

engine = create_engine(
    config.DevelopmentConfig.SQLALCHEMY_DATABASE_URI,
    **config.DevelopmentConfig.SQLALCHEMY_ENGINE_OPTIONS
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
