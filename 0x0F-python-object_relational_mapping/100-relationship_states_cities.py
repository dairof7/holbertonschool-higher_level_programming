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

    _query = s.query(State, City).filter(State.id == City.state_id).all()

    new_State = State(name="California")
    new_City = City(name="San Francisco", state=new_State)
    s.add(new_City)
    s.commit()

    s.close()
