#!/usr/bin/python3

""" Module for State listing"""


import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    usr, pw, db = sys.argv[1:4]
    host = 'localhost'
    port = 3306
    par = f'mysql+mysqldb://{usr}:{pw}@localhost/{db}'

    engine = create_engine(par, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")
