#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
import os

hbnb_storage_type = os.getenv('HBNB_TYPE_STORAGE')


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if hbnb_storage_type is not None and hbnb_storage_type == 'db':
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        '''pass its argument to it base class'''
        super().__init__(*args, **kwargs)
