#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import os
import models

hbnb_storage_type = os.getenv('HBNB_TYPE_STORAGE')

if hbnb_storage_type is not None and hbnb_storage_type == 'db':
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """A base class for all hbnb models"""
    if hbnb_storage_type is not None and hbnb_storage_type == 'db':
        id = Column(String(60), unique=True, nullable=False, primary_key=True)
        created_at = Column(DateTime, nullable=False,
                            default=datetime.utcnow())
        updated_at = Column(DateTime, nullable=False,
                            default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            format = '%Y-%m-%dT%H:%M:%S.%f'
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            for key, value in kwargs.items():
                if key in ('updated_at', 'created_at'):
                    value = datetime.strptime(value, format)
                if key != '__class__':
                    self.__dict__.update({key: value})

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        instance_state = '_sa_instance_state'
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if instance_state in dictionary.keys():
            del dictionary[instance_state]
        return dictionary

    def delete(self):
        '''delete the current instance from the storage'''
        models.storage.delete(self)
