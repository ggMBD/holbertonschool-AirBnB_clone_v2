#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """ The city class, contains state ID and name
    Attributes:
        __tablename__ (str): The name of the table in the database.
        state_id (Column): A foreign key column linking to the\
            id column of the states table.
        name (Column): A column representing the name of the city.
        places (relationship): A one-to-many relationship with the Place model.
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("Place", backref="cities", cascade="delete")
