#!/usr/bin/python3

"""
Module containing a SQL Alchemy query to fetch a specified state
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == '__main__':

    user = argv[1]
    pwd = argv[2]
    db = argv[3]
    state = argv[4]
    host = 'localhost'
    dia = 'mysql+mysqldb'

    connect = '{0}://{1}:{2}@{3}:3306/{4}'.format(dia, user, pwd, host, db)

    engine = create_engine(connect)

    Session = sessionmaker(bind=engine)
    session = Session()

    state_records = session.query(State).filter(State.name == state)

    for state in state_records:
        print("{}: {}".format(state.id, state.name))
