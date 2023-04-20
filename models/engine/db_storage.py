#!/usr/bin/python3
'''this module defines a class to manage storage to a database'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import models
from models.base_model import Base, BaseModel
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
<<<<<<< HEAD
from models.review import Review
=======
>>>>>>> refs/remotes/origin/master
import os


class DBStorage:
    '''This class manages storage of hbnb model in a database'''
    __engine = None
    __session = None
    hbnb_user = os.getenv('HBNB_MYSQL_USER')
    hbnb_pwd = os.getenv('HBNB_MYSQL_PWD')
    hbnb_host = os.getenv('HBNB_MYSQL_HOST')
    hbnb_db = os.getenv('HBNB_MYSQL_DB')
    hbnb_env = os.getenv('HBNB_ENV')

    classes = {
        'State': State, 'City': City, 'User': User,
        'Place': Place, 'Review': Review
    }

    def __init__(self):
        ''' instantiate the database storage'''
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'
            .format(
                self.hbnb_user, self.hbnb_pwd,
                self.hbnb_host, self.hbnb_db
            ),
            pool_pre_ping=True
        )
        try:
            if self.hbnb_env == 'test':
                Base.metadata.drop_all(self.__engine)
        except KeyError:
            pass

    def all(self, cls=None):
        '''
        query all objects depending on the `cls` if not None
        else query all object of BaseModel type.
        '''
        storage = {}
        if cls is None:
            for value in self.classes.values():
                objects = self.__session.query(value).all()
                for obj in objects:
                    key = obj.__class__.__name__ + '.' + obj.id
                    storage[key] = obj
        else:
            if cls in self.classes.values():
                objects = self.__session.query(cls).all()
                for obj in objects:
                    storage[obj.id] = obj
        return storage

    def new(self, obj):
        '''adds a new object to the current db session'''
        if obj is not None:
            self.__session.add(obj)

    def save(self):
        '''commits all changes of the current db session'''
        from sqlalchemy.exc import SQLAlchemyError
        try:
            self.__session.commit()
        except SQLAlchemyError:
            '''ensure the database is still in a consistent state'''
            self.__session.rollback()
            pass

    def delete(self, obj):
        '''delete obj from the current db session'''
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        '''reloads the session from the database'''
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)
