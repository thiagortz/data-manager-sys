from .configuration import config
from .web import Flask
from .routes.route import Route


class Application(object):

    def __init__(self):
        self.config = config.get_config()

    def build_app(self):
        app = Flask(__name__)
        Route(app).register()
        return app

    def start(self):
        is_debug = self.config.mode if self.config.mode else False

        self.build_app().run(self.config.host,
                             self.config.port,
                             debug=is_debug)
