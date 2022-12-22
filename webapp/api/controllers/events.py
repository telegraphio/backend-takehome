from falcon import Request, Response

from datetime import datetime

# from api.db import SQLAlchemy
from api.models.event import Event

class GetEvents:
    """
    Simple get all events data endpoint
    """

    def on_get(self, req: Request, resp: Response):

        posting_date = req.get_param('posting_date') or None

        if posting_date:
            # Parse Posting Date
            try:
                parsed_datetime = datetime.strptime(posting_date, "%Y-%m-%d %H:%M:%S")
                events = [ x.toDict() for x in self.session.query(Event).filter(
                    Event.posting_date==parsed_datetime
                    ).all()]
                resp.media = events
            except ValueError as e:
                resp.media = {"Error Parsing Posting Date": posting_date}
        else:
            resp.media = [ x.toDict() for x in self.session.query(Event).all()]