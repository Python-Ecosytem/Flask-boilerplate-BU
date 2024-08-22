from flask import jsonify
from flask_restx import Namespace, Resource

api = Namespace("hello", "Namespace Description")


@api.route("")
class Hello(Resource):
    def get(self):
        response_body = {"Welcome message": "hello"}
        return jsonify(response_body)
