import os
import json
from datetime import datetime
from functools import partial

import falcon
from falcon import media

from api.config import config_dict
from api.db import SQLAlchemyMiddleware
from api.controllers import setup_routes


class DatetimeEncoder(json.JSONEncoder):
    """Json Encoder that supports datetime objects."""

    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)


def create_app(environment_name):
    configuration = config_dict[environment_name]
    falcon_app = falcon.App(middleware=[SQLAlchemyMiddleware(configuration)])
    json_handler = media.JSONHandler(
        dumps=partial(json.dumps, cls=DatetimeEncoder),
    )
    extra_handlers = {
        "application/json": json_handler,
    }
    setup_routes(falcon_app)
    falcon_app.req_options.media_handlers.update(extra_handlers)
    falcon_app.resp_options.media_handlers.update(extra_handlers)
    falcon_app.req_options.strip_url_path_trailing_slash = True
    return falcon_app, configuration


api, config = create_app(os.getenv("APP_ENV") or "default")
