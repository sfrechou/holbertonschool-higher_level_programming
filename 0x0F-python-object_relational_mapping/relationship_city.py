#!/usr/bin/python3
"""file that contains the class definition of a City"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State
import sqlalchemy



class City(Base):
    """Class City declaration"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
