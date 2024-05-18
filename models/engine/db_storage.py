#!/usr/bin/python3
"""Defines DBStorage class."""
from sqlalchemy import create_engine, URL
from os import getenv
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage():
    """Represents DBStorage Engine"""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize a DBStorage Engine"""

        url_object = URL.create(
            "mysql+mysqldb",
            username=getenv('HBNB_MYSQL_USER', default=None),
            password=getenv('HBNB_MYSQL_PWD', default=None),
            host=getenv('HBNB_MYSQL_HOST', default=None),
            database=getenv('HBNB_MYSQL_DB', default=None)
        )
        self.__engine = create_engine(url_object, pool_pre_ping=True)

        env = getenv('HBNB_ENV')
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls):
        """Query on the current database session"""
        obj_dict = {}
        if cls:
            # Query all objects for the named class
            named_class_objects = self.__session.query(cls).all()
            for obj in named_class_objects:
                key = f'{obj.__class__.__name__}.{obj.id}'
                obj_dict[key] = obj
        else:
            # Query all objects of all classes
            classes = ['User', 'State', 'City', 'Amenity', 'Place', 'Review']
            obj_dict = {}
            for class_name in classes:
                for obj in self.__session.query(class_name).all():
                    key = f'{obj.__class__.__name__}.{obj.id}'
                    obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """Add a new object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database"""
        from models.base_model import BaseModel
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        Base.metadata.create_all(self.__engine)  # Create all the tables
        # Create a configured "Session" class
        session_factory = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False
        )
        # Create a scoped Session
        self.__session = scoped_session(session_factory)
