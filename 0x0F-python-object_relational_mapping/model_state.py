from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """Class State declaration"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))

    def __init__(self, name):
        """Initialization method"""
        self.name = name
