import os

from dotenv import load_dotenv


# Load the default .env file
# load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))


ENV = os.getenv("FLASK_ENV", "development")

if ENV == "production":
    load_dotenv(".env.production")
elif ENV == "testing":
    load_dotenv(".env.tests")
elif ENV == "development":
    load_dotenv(".env.development")


postgres_local_base = os.getenv("DATABASE_URL", None)
rootdir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
    DEBUG = False
    RESTX_MASK_SWAGGER = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///default.db")


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(rootdir, "appDev.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class TestsConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(rootdir, "appTests.db")
    TESTING = True
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")


def init_env(app, config):
    if config == "TESTING":
        app.config.from_object("app.main.config_env.TestsConfig")
        return

    if ENV == "production":
        app.config.from_object("app.main.config_env.ProductionConfig")
    elif ENV == "development":
        app.config.from_object("app.main.config_env.DevelopmentConfig")
    elif ENV == "tests":
        app.config.from_object("app.main.config_env.TestsConfig")
    else:
        app.config.from_object("app.main.config_env.Config")
