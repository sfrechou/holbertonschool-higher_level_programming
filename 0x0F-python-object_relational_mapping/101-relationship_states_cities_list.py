#!/usr/bin/python3
"""
script that lists all State objects, and corresponding
City objects, contained in the database hbtn_0e_101_usa
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

        for instance in session.query(State) \
                               .order_by(State.id):
            print("{}: {}".format(instance.id, instance.name))
            for city in instance.cities:
                print("\t{}: {}".format(city.id, city.name))
        session.close()
