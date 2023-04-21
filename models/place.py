#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
import models
import os

hbnb_storage_type = os.getenv('HBNB_TYPE_STORAGE')


class Place(BaseModel, Base):
    """ A place to stay """
    if hbnb_storage_type == 'db':
        __tablename__ = 'places'
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
        reviews = relationship('Review', backref='place',
                               cascade='all, delete-orphan')
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            '''getter attribute
            returns a list of Review instances with the same
            place id has the current (self) Place instance.
            '''
            all_reviews = models.storage.all(Review)
            result = []
            for review in all_reviews.values():
                if review.place_id == self.id:
                    result.append(review)
            return result

    def __init__(self, *args, **kwargs):
        """initialization method for Place object"""
        super().__init__(*args, **kwargs)
