from falcon import Request, Response

# from api.db import SQLAlchemy
from api.models.waybill import Waybill
from api.models.equipment import Equipment
from api.models.event import Event
from api.models.location import Location

class GetWaybills:
    """
    Simple get all waybills data endpoint
    """

    def on_get(self, _: Request, resp: Response):
        resp.media = [x.toDict() for x in self.session.query(Waybill).all()]

class GetWaybillByID:
    """Simple get single waybill endpoint
    """

    def on_get(self, _: Request, resp: Response, waybill_id):
        
        resp.media = self.session.query(Waybill).get(waybill_id).toDict()


class GetEquipmentByWaybillID:

    def on_get(self, _: Request, resp: Response, waybill_id):
        
        equipment_id = self.session.query(Waybill).get(waybill_id).equipment_id
        equipment = self.session.query(Equipment).filter(Equipment.equipment_id==equipment_id)
        resp.media = [x.toDict() for x in equipment]

class GetEventsByWaybillID:

    def on_get(self, _: Request, resp: Response, waybill_id):
        # We should check that a waybill exists before filtering the Events table
        waybill = self.session.query(Waybill).get(waybill_id)
        events = self.session.query(Event).filter(Event.waybill_id==waybill.id).all()
        resp.media = [x.toDict() for x in events]

class GetLocationsByWaybillID:

    def on_get(self, _: Request, resp: Response, waybill_id):
        
        waybill = self.session.query(Waybill).get(waybill_id)
        locations = self.session.query(Location).filter(
            Location.id.in_([waybill.origin_id, waybill.destination_id])
            )
        resp.media = [x.toDict() for x in locations]