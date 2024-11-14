from __future__ import annotations

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base
engine = create_engine("sqlite:///outpost.db")
metadata = MetaData()

base = declarative_base()