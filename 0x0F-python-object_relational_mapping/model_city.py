#!/usr/bin/python3
"""
Contains City class
"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base


class City(Base):
    """City class with id and name for each city"""
    __tablename__ = 'citites'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
