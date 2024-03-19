#!/usr/bin/python3
"""BaseModel Module for AirBnB Clone Application"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DATETIME
from models import storage_type

Base = declarative_base()


class BaseModel:
    """BaseModel class for AirBnB Clone Application

    Represents the base class for all models in the AirBnB clone application.
    It provides common attributes and methods used by all models.

    Attributes:
        id (str): The unique identifier for each instance of a model.
        created_at (datetime): The date and time when the instance was created.
        updated_at (datetime): The date and time
        when the instance was last updated."""
    id = Column(String(60), nullable=False, primary_key=True, unique=True)
    created_at = Column(DATETIME, nullable=False, default=datetime.utcnow())
    updated_at = Column(DATETIME, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of the BaseModel class."""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key in kwargs:
                if key in ['created_at', 'updated_at']:
                    setattr(self, key, datetime.fromisoformat(kwargs[key]))
                elif key != '__class__':
                    setattr(self, key, kwargs[key])
            if storage_type == 'db':
                if not hasattr(kwargs, 'id'):
                    setattr(self, 'id', str(uuid.uuid4()))
                if not hasattr(kwargs, 'created_at'):
                    setattr(self, 'created_at', datetime.now())
                if not hasattr(kwargs, 'updated_at'):
                    setattr(self, 'updated_at', datetime.now())

    def __str__(self):
        """Returns a string representation of the BaseModel instance."""
        return '[{}] ({}) {}'.format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Saves the current state of the BaseModel instance to the storage."""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the BaseModel instance."""
        dict = self.__dict__.copy()
        dict['__class__'] = self.__class__.__name__
        for k in dict:
            if type(dict[k]) is datetime:
                dict[k] = dict[k].isoformat()
        if '_sa_instance_state' in dict.keys():
            del(dict['_sa_instance_state'])
        return dict

    def delete(self):
        """Deletes the current instance from the storage."""
        from models import storage
        storage.delete(self)
