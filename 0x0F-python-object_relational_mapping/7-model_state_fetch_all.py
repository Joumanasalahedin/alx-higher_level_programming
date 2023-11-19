#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa"""
from model_state import Base, State
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    f"""mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/
    {sys.argv[3]}""")

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
for instance in session.query(State).order_by(State.id):
    print(instance.id, instance.name, sep=': ')
