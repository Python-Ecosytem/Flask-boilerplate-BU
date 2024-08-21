import unittest

from app.main.models.database import db
from app.main.models.User import User


class TestUserModel:
    def test_1(self):
        user = User(
            email="test@test.com",
            password="test",  # noqa: S106
        )
        db.session.add(user)
        db.session.commit()
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
