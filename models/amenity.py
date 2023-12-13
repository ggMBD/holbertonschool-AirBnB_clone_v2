#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv


"""many to many relationship"""
place_amenity = Table(
    "place_amenity",
    Base.metadata,
    Column(
        "place_id",
        String(60),
        ForeignKey("places.id"),
        primary_key=True),
    Column(
        "amenity_id",
        String(60),
        ForeignKey("amenities.id"),
        primary_key=True))



class Amenity(BaseModel, Base):
    """ Amenity class

    Attributes:
        name (str): The name of the amenity.

    Relationships:
        place_amenities (relationship):
            Many-to-Many relationship with the Place class.
    """
    __tablename__ = "amenities"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        place_amenities = relationship(
            "Place",
            secondary="place_amenity",
            viewonly=False,
            back_populates="amenities"
        )
    
    else:
        name = ""
