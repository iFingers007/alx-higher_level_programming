#!/usr/bin/python3

""" Module for State listing"""


import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    usr, pw, db = sys.argv[1:4]
    par = f'mysql+mysqldb://{usr}:{pw}@localhost:3306/{db}'

    engine = create_engine(par, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    match = session.query(State).filter_by(id=2).first()
    match.name = "New Mexico"

    session.commit()

    session.close()
