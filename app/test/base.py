from flask_testing import TestCase

from app.main.app import create_app
from app.main.models.database import db


class BaseTestCase(TestCase):
    def create_app(self):
        app = create_app("TESTING")
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
