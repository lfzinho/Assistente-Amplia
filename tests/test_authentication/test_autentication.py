import datetime
import unittest

from src.authentication.authentication import Authentication
from src.database.database import DatabaseManager


class TestAuthentication(unittest.TestCase):
    """Classe que testa a classe Authentication."""
    def __init__(self, *args, **kwargs):
        super(TestAuthentication, self).__init__(*args, **kwargs)
        self.auth = Authentication()
        self.email = 'email.test@test.com'
        self.password = 'password123'

    def test_constructor(self) -> None:
        """Testa o construtor da classe Authentication."""
        self.assertIsNone(self.auth.uid)

    def test_create_user(self) -> None:
        """Testa o método create_user."""
        self.auth.create_user(self.email, self.password)
        self.assertIsNotNone(self.auth.uid)
        self.auth.delete_user(self.auth.uid)

    def test_get_user_by_email(self) -> None:
        """Testa o método get_user."""
        self.auth.create_user(self.email, self.password)
        user = self.auth.get_user_by_email(self.email)
        self.assertEqual(user.uid, self.auth.uid)
        self.auth.delete_user(self.auth.uid)

    def test_delete_user(self) -> None:
        """Testa o método delete_user."""
        self.auth.create_user(self.email, self.password)
        self.auth.delete_user(self.auth.uid)
        self.assertIsNone(self.auth.uid)

    def test_authenticate(self) -> None:
        """Testa o método authenticate."""
        self.auth.create_user(self.email, self.password)
        self.assertTrue(self.auth.authenticate(self.email, self.password))
        self.auth.delete_user(self.auth.uid)
        self.assertFalse(self.auth.authenticate(self.email, self.password))

    def test_update_user_password(self) -> None:
        """Testa o método update_user_password."""
        self.auth.create_user(self.email, self.password)
        self.auth.update_user_password(self.auth.uid, self.password)
        self.assertTrue(self.auth.authenticate(self.email, self.password))
        self.auth.delete_user(self.auth.uid)

    def test_update_user_email(self) -> None:
        """Testa o método update_user_email."""
        self.auth.create_user(self.email, self.password)
        uid = self.auth.uid
        new_email = 'new'+ self.email
        self.auth.update_user_email(self.auth.uid, new_email)
        self.assertEqual(uid, self.auth.get_user_by_email(new_email).uid)
        self.auth.delete_user(self.auth.uid)


    def test_get_all_users(self) -> None:
        """Testa o método get_all_users."""
        self.auth.create_user(self.email, self.password)
        users = self.auth.get_all_users()
        self.assertTrue(len(users.users) > 0)
        self.auth.delete_user(self.auth.uid)

    def test_authentication_and_database(self) -> None:
        """
        Testa a integração entre a classe Authentication e a
        classe DatabaseManager.
        """
        db = DatabaseManager.instance()

    def test_get_user_by_uid(self) -> None:
        """Testa o método get_user_by_uid."""
        self.auth.create_user(self.email, self.password)
        user = self.auth.get_user_by_uid(self.auth.uid)
        self.assertEqual(user.uid, self.auth.uid)
        self.auth.delete_user(self.auth.uid)

if __name__ == '__main__':
    unittest.main()
