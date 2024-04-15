#!/usr/bin/python3
""" fetch states from db """

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1],
                sys.argv[2],
                sys.argv[3]),
            pool_pre_ping=True
            )
    Base.metadata.create_all(engine)

    # create session
    Session = sessionmaker(bind=engine)
    dbs = Session()

    states = dbs.query(State).filter(State.name == sys.argv[4]).all()
    if (len(states) >= 1):
        for state in states:
            print(f"{state.id}")
    else:
        print("Not found")
