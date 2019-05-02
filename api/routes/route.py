from api.web import Api
from api.resources.hello_world import HelloWorld


class Route(object):
    def __init__(self, app):
        self._app = Api(app, catch_all_404s=True)

    def register(self):
        self._app.add_resource(HelloWorld, "/v1/hello-world")
