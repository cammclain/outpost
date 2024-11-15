# this file contains the models for the agents

from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from ..db import base


class Agent(base):
    __tablename__ = "agents"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    status = Column(String)



class BeaconObject(base):
    __tablename__ = "beacon_objects"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    status = Column(String)
    compatible_agents = Column(String)
    