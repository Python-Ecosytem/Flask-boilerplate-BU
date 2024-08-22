import os

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate

from app.main.extenstions.commands import setup_commands
from app.main.extenstions.setup_admin import setup_admin
from app.main.models.database import db
from app.main.resources import api_blueprint

from .config_env import init_env


def create_app(config=None):
    app = Flask(__name__)
    init_env(app, config)
    app.url_map.strict_slashes = False
    Migrate(app, db, compare_type=True)
    db.init_app(app)
    app.register_blueprint(api_blueprint)
    setup_commands(app)
    setup_admin(app)
    CORS(app)
    return app


if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 3000))
    application = create_app()
    application.run(host="0.0.0.0", port=PORT)
