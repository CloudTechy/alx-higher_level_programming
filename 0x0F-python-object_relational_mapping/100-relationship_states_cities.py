#!/usr/bin/python3
""" fetch states from db """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

from relationship_city import Base, City
from relationship_state import State


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
    session = Session()

    newState = State(name='California')
    newCity = City(name='San Francisco')
    newState.cities.append(newCity)
    session.add(newState)
    session.commit()
