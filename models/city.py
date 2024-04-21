#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """Represents a city, containing state ID and name."""
    # __tablename__ = 'cities'
    # if storage_type == 'db':
    #     name = Column(String(128), nullable=False)
    #     state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    #     places = relationship('Place', backref='cities',
    #                           cascade='all, delete, delete-orphan')
    # else:
    #     name = ''
    #     state_id = ''
    __tablename__ = 'cities'
    if storage_type == 'db':
        id = Column(String(60), primary_key=True) # Ensure this line is present
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship('Place', backref='cities',
                              cascade='all, delete, delete-orphan')
    else:
        id = ''
        name = ''
        state_id = ''
