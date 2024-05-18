#!/usr/bin/python3
"""This module defines a base class for all models in hbnb clone"""
import uuid
from datetime import datetime, timezone
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(
        DateTime,
        default=datetime.now(timezone.utc),
        nullable=False
    )
    updated_at = Column(
        DateTime,
        default=datetime.now(timezone.utc),
        nullable=False
    )

    def __init__(self, *args, **kwargs):
        """Instatantiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now(timezone.utc)
            self.updated_at = datetime.now(timezone.utc)
        else:
            # Set 'id' if not in kwargs
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())

            # Ensure 'created_at' is set
            if 'created_at' in kwargs:
                kwargs['created_at'] = datetime.strptime(
                    kwargs['created_at'],
                    '%Y-%m-%dT%H:%M:%S.%f%z'
                )
            else:
                self.created_at = datetime.now(timezone.utc)

            # Ensure 'updated_at' is set
            if 'updated_at' in kwargs:
                kwargs['updated_at'] = datetime.strptime(
                    kwargs['updated_at'],
                    '%Y-%m-%dT%H:%M:%S.%f%z'
                )
            else:
                self.updated_at = datetime.now(timezone.utc)

            # Remove '__class__' if present in kwargs
            if '__class__' in kwargs:
                del kwargs['__class__']

            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now(timezone.utc)
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        if '_sa_instance_state' in dictionary.keys():
            del dictionary['_sa_instance_state']

        return dictionary

    def delete(self):
        """Deletes the current instance from storage (models.storage)"""
        from models import storage
        storage.delete(self)
