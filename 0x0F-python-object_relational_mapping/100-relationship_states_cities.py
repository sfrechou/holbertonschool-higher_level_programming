#!/usr/bin/python3
"""
script that creates the State “California”
with the City “San Francisco” from the database
"""
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    if len(argv) != 4:
        print("Error")
    else:
        USER = argv[1]
        PASS = argv[2]
        DATAB = argv[3]
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                               .format(USER, PASS, DATAB), pool_pre_ping=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        new_state = State(name="California")
        new_city = City(name="San Francisco")
        new_state.cities.append(new_city)
        session.add(new_state)
        session.add(new_city)
        session.commit()
