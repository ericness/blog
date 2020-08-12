# Testing Flask-RESTX Apps

A common way to provide an interface to data products is to add a RESTful interface using Python Flask.
Flask makes it easy to provide end points to access the data product.

Flask has a number of packages that extend it. On the Data Science team at C.H. Robinson we've found
that one of the most useful of these is Flask-RESTX. This is a maintained fork of the package previously
named Flask-RESTPlus. The documentation describes Flask-RESTX as

> Flask-RESTX is an extension for [Flask](http://flask.pocoo.org/) that adds support for quickly building REST APIs.
Flask-RESTX encourages best practices with minimal setup.
If you are familiar with Flask, Flask-RESTX should be easy to pick up.
It provides a coherent collection of decorators and tools to describe your API
and expose its documentation properly using [Swagger](http://swagger.io/).

Flask-RESTX provides a several helpful features such as
[response marshalling](https://flask-restx.readthedocs.io/en/latest/marshalling.html)
and [automatic Swagger documentation generation](
https://flask-restx.readthedocs.io/en/latest/swagger.html).
While the additional functionality is wonderful, additional explanation for how to
do unit testing for these apps is needed. We'll look at how unit tests for a standard
Flask app can be evolved to cover a Flask-RESTX app.

## Flask Unit Testing

The code for a simple Flask app in file `flask_basic_app.py` looks like:

```python
from flask import Flask

app = Flask(__name__)


@app.route("/hello")
def get():
    return {"hello": "world"}


if __name__ == "__main__":
    app.run()
```

and the unit test for the app looks like:

```python
from testing_flask_restx_apps import flask_basic_app


def test_hello():
    """Should call hello end point"""
    client = flask_basic_app.app.test_client()
    result = client.get("/hello")
    assert result.json == {"hello": "world"}
```

The `test_client` function provides a instance of the Flask `app` that supports
testing routes with `get`, `put` and other methods.

## Flask-RESTX Unit Testing

Once the Flask-RESTX
capabilities are added, testing is quite similar. Here is the [minimal
Flask-RESTX app given in the Quickstart documentation](
https://flask-restx.readthedocs.io/en/latest/quickstart.html#a-minimal-api
)
:

```python
from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)


@api.route("/hello")
class HelloWorld(Resource):
    def get(self):
        return {"hello": "world"}


if __name__ == "__main__":
    app.run()
```

The code is quite similar to the basic Flask app, except that the
decorator is provided by the `api` object and the `get` function is
a method in a `flask_restx.Resource` class. The unit test code for
the "/hello" route looks like:

```python
from testing_flask_restx_apps import flask_basic_restx_app


def test_hello():
    """Should call hello end point"""
    client = flask_basic_restx_app.app.test_client()
    result = client.get("/hello")
    assert result.json == {"hello": "world"}
```

The method of testing also leverages Flask's `test_client` method. The code is
exactly the same as the basic Flask app. So any functionality of the route that
can be tested with Flask can also be tested with Flask-RESTX.

## Flask-RESTX Abstract Factory Unit Testing

Another method of creating a Flask-RESTX app is with [the abstract factory pattern](
https://flask.palletsprojects.com/en/1.1.x/patterns/appfactories/).
This creates the `app` object inside a function rather than within the script
itself.

```python
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
```

Since the `api` object is declared within `create_app`, the end point
routes also need to be declared inside of the function. Then the
`api.route` decorator is available to add routes to the Flask app.

The testing for a Flask-RESTX abstract factory pattern is different than
for a basic Flask-RESTX app. Since the `app` object doesn't exist in the
global context, an easy way to create the object is using a [`pytest` fixture](
https://docs.pytest.org/en/latest/fixture.html
). Fixtures are functions that run before the unit test to create any
objects necessary to perform the test.

```python
import pytest

from testing_flask_restx_apps import flask_restx_app


@pytest.fixture
def client():
    app = flask_restx_app.create_app()
    yield app.test_client()


def test_get_hello(client):
    """Should return expected output from /hello"""
    assert client.get("/hello").json == {"hello": "world"}
```

In this unit test, the `client` function is a `pytest` fixture. Notice how the
test function includes `client` in its parameters. This creates the required
`client` object which `test_get_hello` can then use in the same fashion as
a typical Flask-RESTX unit test.

## Conclusion

Creating unit tests for your Flask app is an important part of the development
process. While using Flask extensions such as Flask-RESTX may seem like it
complicates the testing process, the changes needed to the unit tests are
minor. You can get all the power of Flask-RESTX without giving up the
reliability and maintainability of a well-tested app.

### Resources

[Flask-RESTX Documentation](https://flask-restx.readthedocs.io/en/latest/)
[Testing Flask Applications](https://flask.palletsprojects.com/en/1.1.x/testing/)
[Demystifying Flask's Application Context](
https://hackingandslacking.com/demystifying-flasks-application-context-c7bd31a53817)
