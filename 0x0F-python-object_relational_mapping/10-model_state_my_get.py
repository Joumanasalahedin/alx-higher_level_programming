#!/usr/bin/python3
"""Lists state with name form argument from the database hbtn_0e_6_usa"""
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
    instance = session.query(State).filter(State.name == (sys.argv[4], ))
    if instance:
        print(instance.id)
    else:
        print("Not found")
