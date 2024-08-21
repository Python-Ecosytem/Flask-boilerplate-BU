import os
from dotenv import load_dotenv

# Load the default .env file
load_dotenv()

postgres_local_base = os.environ["DATABASE_URL"]
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
    DEBUG = False
    RESTX_MASK_SWAGGER = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///default.db")


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "flask_boilerplate_main.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    TESTING = True
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = postgres_local_base


ENV = os.getenv("FLASK_ENV", "default")

if ENV == "production":
    load_dotenv(".production.env")
elif ENV == "development":
    load_dotenv(".dev.env")
elif ENV == "testing":
    load_dotenv(".testing.env")
