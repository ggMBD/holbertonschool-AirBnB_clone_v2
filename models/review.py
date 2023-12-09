#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float


class Review(BaseModel, Base):
    """Review class to store review information.
    Attributes:
        __tablename__ (str): The name of the table in the database.
        text (Column):
            A column representing the text content of the revie .
        place_id (Column):
            A foreign key column linking to the id column of the places table.
        user_id (Column):
            A foreign key column linking to the id column of the users table.
    """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
