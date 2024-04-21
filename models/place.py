#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from models.place import place_amenity


if os.getenv("HBNB_TYPE_STORAGE") == "db":
    class Place(BaseModel, Base):
        """ A place to stay """
        __tablename__ = "places"

        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)

        amenities = relationship("Amenity", secondary="place_amenity",
                                 viewonly=False,
                                 back_populates="place_amenities")

        reviews = relationship('Review', back_populates='place',
                               cascade='all, delete-orphan')

        user = relationship('User', back_populates='places')

        city = relationship('City', back_populates='places')
else:
    class Place(BaseModel):
        """ A place to stay """
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenities = []
        reviews = []
        user_id = ""
        city_id = ""

        @property
        def reviews(self):
            """getter funtion to get reviews of certain place"""
            from models import storage
            reviews_dict = storage.all('Review')
            place_reviews = []
            for value in reviews_dict.values():
                if value.place_id == self.id:
                    place_reviews.append(value)
            return place_reviews

        @property
        def amenities(self):
            """getter funtion to get reviews of certain place"""
            from models import storage
            all_amenities = []
            stored = storage.all(Amenity).values()
            for amenity in stored:
                if amenity.id in self.amenity_ids:
                    all_amenities.append(amenity)
            return all_amenities

        @amenities.setter
        def amenities(self, obj):
            """getter funtion to get reviews of certain place"""
            if isinstance(obj, Amenity) and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
