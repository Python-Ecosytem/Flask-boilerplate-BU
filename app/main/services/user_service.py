import datetime
import uuid

from app.main.models.database import db
from app.main.models.User import User


def save_new_user(data: dict[str, str]) -> tuple[dict[str, str], int]:
    user = User.query.filter_by(email=data["email"]).first()
    if not user:
        new_user = User(email=data["email"], password=data["password"], is_active=True)
        save_changes(new_user)
    else:
        response_object = {
            "status": "fail",
            "message": "User already exists. Please Log in.",
        }
        return response_object, 409


def get_all_users():
    return User.query.all()


def get_a_user_by_id(user_id):
    return User.query.filter_by(id=user_id).first()


def save_changes(data: User) -> None:
    db.session.add(data)
    db.session.commit()
