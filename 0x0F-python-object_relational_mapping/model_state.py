#!/usr/bin/python3

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql://root:root@localhost:3306/db")
Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    Base.metadata.create_all(engine)
