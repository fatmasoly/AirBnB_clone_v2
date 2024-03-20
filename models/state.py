#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_type
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State Class Represents a geographical state."""
    __tablename__ = 'states'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade='all,
                              delete, delete-orphan')
    else:
        name = ''

        def cities(self):
            """Getter attribute that returns the list
                of City instances related to the state.
            Returns:
                list: A list of City instances linked to the state."""
            from models import storage
            match_cities = []
            cities = storage.all(City)
            for city in cities.values():
                if city.state_id == self.id:
                    match_cities.append(city)
            return match_cities
