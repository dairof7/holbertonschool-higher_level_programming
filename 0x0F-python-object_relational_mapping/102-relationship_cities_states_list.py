#!/usr/bin/python3
""" print all State from the database"""

import sys
from relationship_state import State
from relationship_city import Base, City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    s = sessionmaker(bind=engine)()

    _query = s.query(City).order_by(City.id)

    for city in _query:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    s.close()
