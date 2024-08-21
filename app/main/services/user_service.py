import datetime
import uuid

from app.main.models.database import db
from app.main.models.User import User


def save_new_user(data: dict[str, str]) -> tuple[dict[str, str], int]:
    user = User.query.filter_by(email=data["email"]).first()
    if not user:
        new_user = User(
            public_id=str(uuid.uuid4()),
            email=data["email"],
            username=data["username"],
            password=data["password"],
            registered_on=datetime.datetime.utcnow(),
        )
        save_changes(new_user)
    else:
        response_object = {
            "status": "fail",
            "message": "User already exists. Please Log in.",
        }
        return response_object, 409


def get_all_users():
    return User.query.all()


def get_a_user(public_id):
    return User.query.filter_by(public_id=public_id).first()


def save_changes(data: User) -> None:
    db.session.add(data)
    db.session.commit()
