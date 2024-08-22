from flask import request
from flask_restx import Resource

from app.main.dto.UserDto import UserDto

from ..services.user_service import get_a_user_by_id, get_all_users, save_new_user

api = UserDto.api
_user = UserDto.user


@api.route("/")
class UserList(Resource):
    @api.doc("list_of_registered_users")
    @api.marshal_list_with(_user, envelope="data")
    def get(self):
        """List all registered users"""
        return get_all_users()

    @api.expect(_user, validate=True)
    @api.response(201, "User successfully created.")
    @api.doc("create a new user")
    def post(self) -> tuple[dict[str, str], int]:
        """Creates a new User"""
        data = request.json
        return save_new_user(data=data)


@api.route("/<user_id>")
@api.param("user_id", "The User identifier")
@api.response(404, "User not found.")
class User(Resource):
    @api.doc("get a user")
    @api.marshal_with(_user)
    def get(self, user_id):
        """get a user given its identifier"""
        user = get_a_user_by_id(user_id)
        if not user:
            api.abort(404)
        else:
            return user
