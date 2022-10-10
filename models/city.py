#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from models.state import State
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    state_id = Column(String(128), ForeignKey(State.id), nullable=False)
    name = Column(String(60), nullable=False)
