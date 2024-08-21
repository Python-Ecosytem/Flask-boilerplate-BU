import unittest

from app.main.models.database import db
from app.main.models.User import User
from app.test.base import BaseTestCase


class TestUserModel(BaseTestCase):
    def test_1(self):
        user = User(
            email="test@test.com",
            password="test",  # noqa: S106
        )

        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
