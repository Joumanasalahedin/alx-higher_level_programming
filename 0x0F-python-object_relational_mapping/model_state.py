#!/usr/bin/python3
"""
Contains State class and Base, an instance of declarative_base()
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.orm import declarative_base

metadata = MetaData()
Base = declarative_base()
Base.metdata = metadata


class State(Base):
    """state class with id and name for each state"""
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
