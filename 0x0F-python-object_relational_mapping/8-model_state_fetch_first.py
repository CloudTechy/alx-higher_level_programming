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

    state = dbs.query(State).first()
    if (state):
        print(state.id, state.name, sep=": ")
    else:
        print("Nothing")
