#!/usr/bin/python3
"""Prints all cities in the database hbtn_0e_6_usa"""
from model_state import Base, State
from model_city import City
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in (session.query(State.name, City.id, City.name)
                     .filter(State.id == City.state_id).all()):
        print(instance[0] + ": (" + str(instance[1]) + ") " + instance[2])
