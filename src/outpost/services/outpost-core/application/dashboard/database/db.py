from __future__ import annotations

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base
from config.config import settings


# create the engine
engine = create_engine(settings.DATABASE_URL)

# create the metadata
metadata = MetaData()

base = declarative_base()