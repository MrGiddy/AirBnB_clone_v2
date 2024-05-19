#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, INTEGER, FLOAT, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.amenity import Amenity


place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
)

class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(INTEGER, default=0, nullable=False)
    number_bathrooms = Column(INTEGER, default=0, nullable=False)
    max_guest = Column(INTEGER, default=0, nullable=False)
    price_by_night = Column(INTEGER, default=0, nullable=False)
    latitude = Column(FLOAT, nullable=True)
    longitude = Column(FLOAT, nullable=True)

    reviews = relationship('Review', cascade='all, delete', backref='place')
    amenities = relationship(
        'Amenity',
        secondary='place_amenity',
        viewonly=False
    )

    amenity_ids = []

    # For FileStorage relationship between Place and Review
    @property
    def reviews(self):
        """Retrieves all places with ids matching the current place's id"""
        from models import storage

        # Retrieve all instances of place from storage
        all_places = storage.all(Place)

        # Filter to get places with ids matching the current place's id
        return [plc for plc in all_places.values() if plc.place_id == self.id]

    @property
    def amenities(self):
        """
        Retrieves all Amenity instances that are linked to the current Place
        """
        from models import storage

        all_amenities = storage.all(Amenity)
        filtered = []
        for amenity in all_amenities.values():
            if amenity.id in self.amenity_ids:
                filtered.append(amenity)
        return filtered

    @amenities.setter
    def amenities(self, obj):
        """Adds an id of an Amenity to the list amenity_ids"""

        if isinstance(obj, Amenity):
            if obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
