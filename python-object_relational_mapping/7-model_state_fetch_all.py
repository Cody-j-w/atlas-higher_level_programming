#!/usr/bin/python3

"""
Module containing a SQL Alchemy query to fetch all states in an arg-provided DB
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if len(argv) > 1:
    user = argv[1]
if len(argv) > 2:
    pwd = argv[2]
if len(argv) > 3:
    db = argv[3]

engine = create_engine('mysql+mysqldb://{0}:{1}@localhost:3306/{2}'.format(user, pwd, db))

Session = sessionmaker(bind=engine)
session = Session()

state_records = session.query(State).all()

for state in state_records:
    print("{}: {}".format(state.id, state.name))