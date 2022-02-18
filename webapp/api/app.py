import os

import falcon

from api.config import config_dict
from api.db import SQLAlchemyMiddleware
from api.controllers import setup_routes

def create_app(environment_name):
    configuration = config_dict[environment_name]
    falcon_app = falcon.App(middleware=[
        SQLAlchemyMiddleware(configuration)
    ])
    setup_routes(falcon_app)
    return falcon_app, configuration

api, config = create_app(os.getenv('APP_ENV') or 'default')
