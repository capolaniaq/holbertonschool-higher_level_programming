#!/usr/bin/python3
"""Start link class to table in database """


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql://root:root@localhost:3306/db")
Base = declarative_base()


class State(Base):
    """firts class state inherits base"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
