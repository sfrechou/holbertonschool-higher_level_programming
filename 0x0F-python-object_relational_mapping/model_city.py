from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class City(Base):
    """Class City declaration"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    state_id = Column(Integer, ForeignKey('states.id'))

    def __init__(self, name):
        """Initialization method"""
        self.name = name
