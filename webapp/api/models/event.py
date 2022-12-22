from sqlalchemy import Column, DateTime, Integer, String

from .base import Base, BaseMixin

class Event(BaseMixin, Base):
    """Model for provided data/events.csv"""
    
    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    equipment_id = Column(String)
    sighting_date = Column(DateTime)
    sighting_event_code = Column(Integer)
    reporting_railroad_scac = Column(String)
    posting_date = Column(DateTime)
    from_mark_id = Column(String)
    load_empty_status = Column(String)
    sighting_claim_code  = Column(String)
    sighting_event_code_text  = Column(String)
    train_id  = Column(String)
    train_alpha_code  = Column(String)
    location_id = Column(Integer)
    waybill_id = Column(Integer)
