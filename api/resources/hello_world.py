from api.web import Resource


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
