"""Hello World Resource


Run:

    flask run

Test:

    $ curl -X GET http://127.0.0.1:5000
    Hello, World!
"""

from flask import Flask
from flask_resources import Resource, ResourceConfig, route


# Example of a resource
class HelloWorldResource(Resource):
    def hello_world(self):
        return "Hello, World!\n"

    def create_url_rules(self):
        return [
            route("GET", "/", self.hello_world),
        ]

# Example of a resource config used for dependency injection
class Config(ResourceConfig):
    blueprint_name = "hello"

# Create an instance of the resource by injecting the config
resource = HelloWorldResource(Config)

app = Flask('test')

# as_blueprint() will call create_url_rules() in order to get the routing
app.register_blueprint(resource.as_blueprint())
