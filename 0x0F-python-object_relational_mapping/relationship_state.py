#!/usr/bin/python3
""" class State and an instance Base = declarative_base()"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City


class State(Base):
    """State class"""
    __tablename__ = 'states'

    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        autoincrement="auto"
    )

    name = Column(
        String(128),
        nullable=False
    )

    cities = relationship("City", backref="state", cascade="all, delete")
