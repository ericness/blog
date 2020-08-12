from testing_flask_restx_apps import flask_basic_restx_app


def test_hello():
    """Should call hello end point"""
    client = flask_basic_restx_app.app.test_client()
    result = client.get("/hello")
    assert result.json == {"hello": "world"}
