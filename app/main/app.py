import os
from flask import Flask, request, jsonify, url_for, send_from_directory
from app.main.models.database import db
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Resource, Api

from app.main.extenstions.setup_admin import setup_admin
from app.main.extenstions.commands import setup_commands
from app.main.resources.user_resource import api
from flask_swagger import swagger
from app.main.resources import blueprint
from flask_cors import CORS
# CORS(api)

ENV = "development" if os.getenv("FLASK_DEBUG") == "1" else "production"

app = Flask(__name__)

app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url.replace("postgres://", "postgresql://")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
MIGRATE = Migrate(app, db, compare_type=True)
db.init_app(app)


app.register_blueprint(blueprint)

setup_commands(app)
setup_admin(app)


if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 3001))
    app.run(host="0.0.0.0", port=PORT, debug=True)
