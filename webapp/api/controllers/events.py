from falcon import Request, Response

from datetime import datetime

# from api.db import SQLAlchemy
from api.models.event import Event

class GetEvents:
    """
    Simple get all events data endpoint
    """

    def on_get(self, req: Request, resp: Response):

        posting_date_start = req.get_param('posting_date_start') or None
        posting_date_end = req.get_param('posting_date_end') or None
        posting_date = req.get_param('posting_date') or None

        if posting_date:
            # Parse Posting Date
            try:
                parsed_datetime = datetime.strptime(posting_date, "%Y-%m-%d %H:%M:%S")
                resp.media = [ x.toDict() for x in self.session.query(Event).filter(posting_date==parsed_datetime).all() ]

            except ValueError as e:
                resp.media = {"Error Parsing Posting Date": posting_date}
            # return filtered by posting date data
        else:
            resp.media = [ x.toDict() for x in self.session.query(Event).all()]