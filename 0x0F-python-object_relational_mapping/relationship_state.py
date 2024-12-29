#!/usr/bin/python3
"""
Contains the class definition of a State with relationship
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """State class with cities relationship

    Attributes:
        id (int): The state's id
        name (str): The state's name
        cities (relationship): relationship to City class
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")
