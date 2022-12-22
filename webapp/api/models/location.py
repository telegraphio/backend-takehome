from sqlalchemy import Column, DateTime, Integer, String

from .base import Base, BaseMixin

class Location(BaseMixin, Base):
    """Model for provided data/locations.csv"""
    
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True)
    city = Column(String)
    city_long = Column(String)
    station = Column(String)
    fsac = Column(String) # could be a int w/ more context
    scac = Column(String)
    splc = Column(String) # could be a int w/ more context
    state = Column(String)
    time_zone = Column(String)
    # If geospatial computations are important
    # lat/lng should be PostGIS geog items
    # SRID=4326;POINT(longitude latitude)'
    longitude = Column(String)
    latitude = Column(String)
    country = Column(String)