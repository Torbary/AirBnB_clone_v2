#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
import os

hbnb_storage_type = os.getenv('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """ State class """
    if hbnb_storage_type is not None and hbnb_storage_type == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade='all, delete-orphan')
    else:
        name = ""

        @property
        def cities(self):
            '''
            list of City instances with state_id == current State.id
            '''
            all_cities = models.storage.all(City)
            result = []
            for city in all_cities.values():
                if city.state_id == self.id:
                    result.append(city)
            return result

    def __init__(self, *args, **kwargs):
        '''pass its argument to it base class'''
        super().__init__(*args, **kwargs)
