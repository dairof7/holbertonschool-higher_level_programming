#!/usr/bin/python3
""" print all State from the database"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    s = sessionmaker(bind=engine)()

    _query = s.query(State, City).filter(State.id == City.state_id).all()

    for state, cities in _query:
        print("{}: ({}) {}".format(state.name, cities.id, cities.name))
    s.close()
