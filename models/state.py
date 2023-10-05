#!/usr/bin/python3
""" State Module for HBNB project for AirBNB_clone_v2"""


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.engine.file_storage import FileStorage
from os import getenv


class State(BaseModel, Base):
    """ State class definition in the next line"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade="all, delete")

    if getenv("HBNB_TYPE_STORAGE") != 'db':
        @property
        def cities(self):
            from models import storage
            from models.city import City
            """Get a list of all related City objects."""
            city_list = []
            for city in list(storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
