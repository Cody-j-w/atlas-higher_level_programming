#!/usr/bin/python3

"""
Module containing a SQL Alchemy query to delete all rows containing 'a'
"""
from sqlalchemy import create_engine, delete
from sqlalchemy.orm import sessionmaker
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

    deleted_states = State.__table__.delete().where(State.name.contains('a'))
    session.execute(deleted_states)
    session.commit()
    session.close()
