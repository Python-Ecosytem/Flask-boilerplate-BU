import os

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from app.main.models.database import db
from app.main.models.User import User


def setup_admin(app):
    app.secret_key = os.environ.get("FLASK_APP_KEY", "sample key")
    # app.config["FLASK_ADMIN_SWATCH"] = "readable"
    app.config["FLASK_ADMIN_SWATCH"] = "flatly"
    admin = Admin(app, name="Admin", template_mode="bootstrap3")
    admin.add_view(ModelView(User, db.session))
