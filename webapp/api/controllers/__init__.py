import falcon

# import your controllers

from api.controllers.health import (
    PingHandler,
)

# add your routes
def setup_routes(app: falcon.App):
    app.add_route("/health/ping", PingHandler())