import os

from dotenv import load_dotenv

# Load the default .env file
load_dotenv()


ENV = os.getenv("FLASK_ENV", "default")

if ENV == "production":
    load_dotenv(".production.env")
elif ENV == "testing":
    load_dotenv(".testing.env")
elif ENV == "development":
    load_dotenv(".development.env")


postgres_local_base = os.environ["DATABASE_URL"]
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
    DEBUG = False
    RESTX_MASK_SWAGGER = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///default.db")


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "appdev.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    TESTING = True
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")


def init_env(app):
    if ENV == "production":
        app.config.from_object("app.main.config_env.ProductionConfig")
    elif ENV == "development":
        app.config.from_object("app.main.config_env.DevelopmentConfig")
    elif ENV == "testing":
        app.config.from_object("app.main.config_env.TestingConfig")
    else:
        app.config.from_object("app.main.config_env.Config")
