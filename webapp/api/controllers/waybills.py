from datetime import datetime

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
    """Simple get single waybill endpoint"""

    def on_get(self, _: Request, resp: Response, waybill_id):

        resp.media = self.session.query(Waybill).get(waybill_id).toDict()


class GetEquipmentByWaybillID:
    def on_get(self, _: Request, resp: Response, waybill_id):

        equipment_id = self.session.query(Waybill).get(waybill_id).equipment_id
        equipment = self.session.query(Equipment).filter(
            Equipment.equipment_id == equipment_id
        )
        resp.media = [x.toDict() for x in equipment]


class GetEventsByWaybillID:
    def on_get(self, req: Request, resp: Response, waybill_id):
        posting_date = req.get_param("posting_date") or None
        waybill = self.session.query(Waybill).get(waybill_id)
        if posting_date:
            # Parse Posting Date
            try:
                parsed_datetime = datetime.strptime(posting_date, "%Y-%m-%d %H:%M:%S")
                events = [
                    x.toDict()
                    for x in self.session.query(Event)
                    .filter(
                        Event.posting_date == parsed_datetime
                        and Event.waybill_id == waybill.id
                    )
                    .all()
                ]
                resp.media = events
            except ValueError as e:
                resp.media = {"Error Parsing Posting Date": posting_date}
        else:
            events = (
                self.session.query(Event).filter(Event.waybill_id == waybill.id).all()
            )
            resp.media = [x.toDict() for x in events]


class GetLocationsByWaybillID:
    def on_get(self, _: Request, resp: Response, waybill_id):

        waybill = self.session.query(Waybill).get(waybill_id)
        locations = self.session.query(Location).filter(
            Location.id.in_([waybill.origin_id, waybill.destination_id])
        )
        resp.media = [x.toDict() for x in locations]


class GetRouteByWaybillID:
    def on_get(self, _: Request, resp: Response, waybill_id):

        waybill = self.session.query(Waybill).get(waybill_id)
        resp.media = waybill.routes


class GetPartiesByWaybillID:
    def on_get(self, _: Request, resp: Response, waybill_id):

        waybill = self.session.query(Waybill).get(waybill_id)
        resp.media = waybill.parties
