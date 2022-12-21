from sqlalchemy import Column, DateTime, Integer, String

from .base import Base

class Equipment(Base):
    """Model for provided data/equipment.csv"""
    
    __tablename__ = "equipment"

    id = Column(Integer, primary_key=True)
    customer = Column(String)
    fleet = Column(String)
    equipment_id = Column(String)
    equipment_status = Column(String)
    # Time in UTC or local time w/ no timezone?
    date_added = Column(DateTime)
    date_removed = Column(DateTime)
