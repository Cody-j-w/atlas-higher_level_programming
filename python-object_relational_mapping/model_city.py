#!/usr/bin/python3

"""
Module containing State SQLAlchemy definition
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from model_state import State, Base


class City(Base):
    """
    City SQLAlchemy model
    Attributes:
        __tablename__: the name of the table
        id: an identifying integer
        name: the name of the city
        state_id: the id of the city's state
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))

    state = relationship("State", back_populates="cities")
