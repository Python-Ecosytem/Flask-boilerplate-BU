import os

from dotenv import load_dotenv

# Load the default .env file
load_dotenv()


ENV = os.getenv("FLASK_ENV", "development")

if ENV == "production":
    load_dotenv(".env.production")
elif ENV == "testing":
    load_dotenv(".env.tests")
elif ENV == "development":
    load_dotenv(".env.development")


postgres_local_base = os.getenv("DATABASE_URL", None)
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
    DEBUG = False
    RESTX_MASK_SWAGGER = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///default.db")


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "appDev.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestsConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "appTests.db")
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
    elif ENV == "tests":
        app.config.from_object("app.main.config_env.TestsConfig")
    else:
        app.config.from_object("app.main.config_env.Config")
