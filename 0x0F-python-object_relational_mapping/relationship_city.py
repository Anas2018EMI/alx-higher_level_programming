#!/usr/bin/python3
"""
Contains the class definition of a City with relationship
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State


class City(Base):
    """City class with state relationship

    Attributes:
        id (int): The city's id
        name (str): The city's name
        state_id (int): The city's state id
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
