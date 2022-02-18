from falcon import Request, Response

class PingHandler:
    """
    Simple ping endpoint
    """

    def on_get(self, _: Request, resp: Response):
        resp.media = {"ping": True}