A common way to provide an interface to data products is to add a RESTful interface using Python Flask.
This library makes it easy to provide end points to access the data product.

Flask has a number of packages that extend it. On the Data Science team at C.H. Robinson we've found
that one of the most useful of these is Flask-RESTX. This is a maintained fork of the package previously
named Flask-RESTPlus. The documentation describes Flask-RESTX as

> Flask-RESTX is an extension for [Flask](http://flask.pocoo.org/) that adds support for quickly building REST APIs.
Flask-RESTX encourages best practices with minimal setup.
If you are familiar with Flask, Flask-RESTX should be easy to pick up.
It provides a coherent collection of decorators and tools to describe your API
and expose its documentation properly using [Swagger](http://swagger.io/).

While Flask-RESTX provides a several helpful features such as
[response marshalling](https://flask-restx.readthedocs.io/en/latest/marshalling.html)
and [automatic Swagger documentation generation](
https://flask-restx.readthedocs.io/en/latest/swagger.html).

While the additional functionality is wonderful, it creates more complexity with creating unit tests.


[Flask-RESTX Documentation](https://flask-restx.readthedocs.io/en/latest/)
[Testing Flask Applications](https://flask.palletsprojects.com/en/1.1.x/testing/)
[Demystifying Flask's Application Context](
https://hackingandslacking.com/demystifying-flasks-application-context-c7bd31a53817)
