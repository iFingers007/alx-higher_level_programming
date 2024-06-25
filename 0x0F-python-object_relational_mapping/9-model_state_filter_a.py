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

    matchs = (
        session.query(State)
        .filter(State.name.like('%a%'))
        .order_by(State.id)
        .all()
    )

    for match in matchs:
        print(f"{match.id}: {match.name}")
