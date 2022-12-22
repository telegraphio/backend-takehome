from sqlalchemy import Column, DateTime, Integer, JSON, String

from .base import Base, BaseMixin

class Waybill(BaseMixin, Base):
    """Model for provided data/waybills.csv"""
    
    __tablename__ = "waybills"

    id = Column(Integer, primary_key=True)
    equipment_id = Column(String)
    waybill_date = Column(DateTime) # Could be date field with more context
    waybill_number = Column(Integer)
    created_date = Column(DateTime)
    billing_road_mark_name = Column(String)
    waybill_source_code = Column(String)
    load_empty_status = Column(String)
    origin_mark_name = Column(String)
    destination_mark_name = Column(String)
    sending_road_mark = Column(String)
    bill_of_lading_number = Column(String)
    bill_of_lading_date = Column(DateTime)
    equipment_weight = Column(String)
    tare_weight = Column(String)
    allowable_weight = Column(String)
    dunnage_weight = Column(String)
    equipment_weight_code = Column(String)
    commodity_code = Column(Integer)
    commodity_description = Column(String)
    origin_id = Column(Integer)
    destination_id = Column(Integer)
    routes = Column(JSON)
    parties = Column(JSON)
