#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_type
from models import City
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, 


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade='all, delete, delete-orphan')
    else:
        name = ""


        def cities(self):

            from models import storage
            linked_cities = []
            cities = storage.all(City)
            for city in cities.values():
                if city.state_id == self.id:
                    linked_cities.append(city)
            return linked_cities
