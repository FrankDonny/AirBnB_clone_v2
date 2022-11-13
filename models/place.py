# #!/usr/bin/python3
# """ Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from os import getenv

metadata = Base.metadata
place_amenity = Table("place_amenity", metadata,
                      Column("place_id", String(60), ForeignKey("places.id"),
                             primary_key=True, nullable=False),
                      Column("amenity_id", String(60), ForeignKey("amenities.id"),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", cascade="all, delete",
                               backref="place")
        amenities = relationship("Amenity", secondary=place_amenity, viewonly=False,
                                 backref="place_amenities")
    else:
        @property
        def reviews(self):
            """getter to return review objects"""
            from models import storage
            from models.review import Review
            return [value for value in storage.all(Review).values()
                    if value.place_id == self.id]

        @property
        def amenities(self):
            """getter to return Amenity objects"""
            from models import storage
            from models.amenity import Amenity
            return [value for value in storage.all(Amenity).values()
                    if value.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, obj):
            """setter for appending object id"""
            from models.amenity import Amenity
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
