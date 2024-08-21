import unittest

from app.main.models.database import db
from app.main.models.User import User
from app.test.base import BaseTestCase


class TestUserModel(BaseTestCase):
    def test_1(self):
        user = User(
            email="user@mail.org",
            password="password",  # noqa: S106
            is_active=True,
        )
        db.session.add(user)
        db.session.commit()
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
