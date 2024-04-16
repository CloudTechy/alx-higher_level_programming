#!/usr/bin/python3
""" create state model """

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class City(Base):
    """ defines a state class orm """
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
    state = relationship("State", back_populates="cities")
