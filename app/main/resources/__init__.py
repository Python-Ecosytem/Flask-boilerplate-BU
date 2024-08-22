from flask import Blueprint
from flask_restx import Api

from .hello_api import api as hello_ns
from .user_resource import api as user_ns

api_blueprint = Blueprint("api", __name__, url_prefix="/api")

api = Api(
    api_blueprint,
    title="FLASK API",
    version="1.0",
    description="A boilerplate for API flask",
)

api.add_namespace(user_ns)
api.add_namespace(hello_ns)
