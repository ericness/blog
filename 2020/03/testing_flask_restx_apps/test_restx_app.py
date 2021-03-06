import pytest

from testing_flask_restx_apps import flask_restx_app


@pytest.fixture
def client():
    app = flask_restx_app.create_app()
    yield app.test_client()


def test_get_hello(client):
    """Should return expected output from /hello"""
    assert client.get("/hello").json == {"hello": "world"}
