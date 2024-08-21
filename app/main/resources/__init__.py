from flask import Blueprint
from flask_restx import Api

from .user_resource import api as user_ns

blueprint = Blueprint("api", __name__, url_prefix="/api")
api = Api(
    blueprint,
    title="FLASK API",
    version="1.0",
    description="A boilerplate for flask API",
)

api.add_namespace(user_ns)
