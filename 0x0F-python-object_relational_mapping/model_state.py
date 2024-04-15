#!/usr/bin/python3
""" create state model """

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()


class State(Base):
    """ defines a state class orm """
    __tablename__ = 'states'
    id = Column(
            Integer,
            primary_key=True,
            unique=True,
            nullable=False
            )
    name = Column(
            String(128),
            nullable=False
            )
