#!/usr/bin/python3
""" print all State from the database"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]
    STATE = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    s = sessionmaker(bind=engine)()

    _query = s.query(State).filter(State.name == STATE).first()
    if _query:
        print(_query.id)
    else:
        print('Not found')

    s.close()
