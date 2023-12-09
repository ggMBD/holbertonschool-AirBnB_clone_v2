#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """Represents a user for a MySQL database.

    Attributes:
        email (str): The email address of the user.
        password (str): The password associated with the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.

    Relationships:
        places (relationship): One-to-Many relationship with the Place class.
        reviews (relationship): One-to-Many relationship with the Review class.
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")
