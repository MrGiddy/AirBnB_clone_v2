#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    # for DBStorage relationship between State and City
    cities = relationship('City', cascade='all, delete', backref='state')

    # for fileStorage relationship between State and City
    @property
    def cities(self):
        """Retrieves cities matching the current state's id"""
        from models import storage

        # Retrieve all instances of City from storage
        all_cities = storage.all(City)
        # Filter to get cities with ids matching the current state's id
        return [cty for cty in all_cities.values() if cty.state_id == self.id]
