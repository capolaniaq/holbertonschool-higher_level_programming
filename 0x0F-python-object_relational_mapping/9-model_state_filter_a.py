#!/usr/bin/python3
"""Start link class to table in database """

from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine


if __name__ == "__main__":
    user = argv[1]
    password = argv[2]
    database = argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        user, password, database), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()
    for state in states:
        if 'a' in state.name:
            print("{}: {}".format(state.id, state.name))

    session.close()
