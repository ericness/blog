from flask import Flask
from flask_restx import Api, Resource


def create_app():
    """Initialize the Flask app"""
    app = Flask(__name__)
    api = Api()

    with app.app_context():
        api.init_app(app)

    @api.route("/hello")
    class HelloWorld(Resource):
        def get(self):
            return {"hello": "world"}

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
