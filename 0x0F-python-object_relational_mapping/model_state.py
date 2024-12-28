#!/usr/bin/python3
"""
    contains the class definition of a State
"""
from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """_summary_

    Args:
        Base (_type_): _description_
    """

    __tablename__ = 'states'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
