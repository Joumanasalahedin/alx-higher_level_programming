#!/usr/bin/python3
"""Adds State object to the database hbtn_0e_6_usa"""
from model_state import Base, State
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(State(name='Louisiana'))
    new_state = session.query(State).filter_by(name='Louisiana').first()
    print(new_state.id)
    session.commit()
