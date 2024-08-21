import os

from flask import Flask
from flask_migrate import Migrate

from app.main.extenstions.commands import setup_commands
from app.main.extenstions.setup_admin import setup_admin
from app.main.models.database import db
from app.main.resources import blueprint

from .config_env import init_env

app = Flask(__name__)
init_env(app)
app.url_map.strict_slashes = False

MIGRATE = Migrate(app, db, compare_type=True)
db.init_app(app)


app.register_blueprint(blueprint)

setup_commands(app)
setup_admin(app)


if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 3001))
    app.run(host="0.0.0.0", port=PORT)
