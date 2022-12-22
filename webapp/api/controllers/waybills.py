from falcon import Request, Response

# from api.db import SQLAlchemy
from api.models.waybill import Waybill

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