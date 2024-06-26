#!/usr/bin/python3
""" create city model """

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey

Base = declarative_base()


class City(Base):
    """ defines a city class orm """
    __tablename__ = 'cities'
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
    state_id = Column(
            Integer,
            ForeignKey("states.id"),
            nullable=False
            )
