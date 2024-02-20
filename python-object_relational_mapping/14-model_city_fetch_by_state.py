#!/usr/bin/python3

"""
Module containing a SQL Alchemy query to fetch all cities and their respective
states
"""
from sqlalchemy import create_engine, delete, asc
from sqlalchemy.orm import sessionmaker
from model_city import City
from model_state import Base, State
from sys import argv

if __name__ == '__main__':

    user = argv[1]
    pwd = argv[2]
    db = argv[3]
    host = 'localhost'
    dia = 'mysql+mysqldb'

    connect = '{0}://{1}:{2}@{3}:3306/{4}'.format(dia, user, pwd, host, db)

    engine = create_engine(connect)

    Session = sessionmaker(bind=engine)
    session = Session()

    cs = (session.query(State, City).filter(State.id == City.state_id).all())

    for s, c in cs:
        print("{0}: ({1}) {2}".format(s.name, c.id, c.name))
