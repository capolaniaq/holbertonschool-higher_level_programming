#!/usr/bin/python3
"""Start link class to table in database """


from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Firts class state inherits to Base"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
