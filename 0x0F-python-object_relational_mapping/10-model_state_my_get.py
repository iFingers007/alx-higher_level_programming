#!/usr/bin/python3

""" Module for State listing"""


import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    if len(sys.argv) != 5:
        sys.exit(1)

    usr, pw, db, sn = sys.argv[1:5]
    par = f'mysql+mysqldb://{usr}:{pw}@localhost:3306/{db}'

    engine = create_engine(par, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    match = session.query(State).filter(State.name == sn).first()

    if match:
        print(f"{match.id}")
    else:
        print("Not Found")
