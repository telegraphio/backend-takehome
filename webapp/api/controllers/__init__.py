import falcon

# import your controllers

from api.controllers.health import (
    PingHandler,
)

from api.controllers.equipment import (
    GetEquipment,
)
from api.controllers.events import (
    GetEvents,
)
from api.controllers.locations import (
    GetLocations,
)
from api.controllers.waybills import (
    GetWaybills,
    GetWaybillByID,
    GetEquipmentByWaybillID,
    GetEventsByWaybillID,
    GetLocationsByWaybillID,
    GetRouteByWaybillID,
    GetPartiesByWaybillID
)

# add your routes
def setup_routes(app: falcon.App):
    app.add_route("/health/ping", PingHandler())
    app.add_route("/equipment", GetEquipment())
    app.add_route("/events", GetEvents())
    app.add_route("/locations", GetLocations())
    app.add_route("/waybills", GetWaybills())
    app.add_route("/waybills/{waybill_id}", GetWaybillByID())
    app.add_route("/waybills/{waybill_id}/equipment", GetEquipmentByWaybillID())
    app.add_route("/waybills/{waybill_id}/events", GetEventsByWaybillID())
    app.add_route("/waybills/{waybill_id}/locations", GetLocationsByWaybillID())
    app.add_route("/waybills/{waybill_id}/route", GetRouteByWaybillID())
    app.add_route("/waybills/{waybill_id}/parties", GetPartiesByWaybillID())
