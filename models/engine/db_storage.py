#!/usr/bin/python3
"""New engine DBStorage"""
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import *


class DBStorage():
    """Private class attributes:"""
    __engine = None
    __session = None

    def __init__(self):
        """create the engine """
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                getenv("HBNB_MYSQL_USER"),
                getenv("HBNB_MYSQL_PWD"),
                getenv("HBNB_MYSQL_HOST"),
                getenv("HBNB_MYSQL_DB")
            ),
            pool_pre_ping=True
        )
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        pass

    def new(self, obj):
        pass

    def save(self):
        pass

    def delete(self, obj=None):
        pass

    def reload(self):
        pass

