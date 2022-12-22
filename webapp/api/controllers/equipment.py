from falcon import Request, Response

# from api.db import SQLAlchemy
from api.models.equipment import Equipment

class GetEquipment:
    """
    Simple get all equipment data endpoint
    """

    def on_get(self, _: Request, resp: Response):
        all_equipment = [x.toDict() for x in self.session.query(Equipment).all()]
        resp.media = all_equipment