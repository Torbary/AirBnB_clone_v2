#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
import os
import models

hbnb_storage_type = os.getenv('HBNB_TYPE_STORAGE')


class Amenity(BaseModel, Base):
    if hbnb_storage_type == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ''

    def __init__(self, *args, **kwargs):
        '''initializes Amenity object'''
        super().__init__(*args, **kwargs)
