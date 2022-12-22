from falcon import Request, Response

# from api.db import SQLAlchemy
from api.models.event import Event

class GetEvents:
    """
    Simple get all events data endpoint
    """

    def on_get(self, _: Request, resp: Response):
        resp.media = [x.toDict() for x in self.session.query(Event).all()]