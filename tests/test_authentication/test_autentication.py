import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

import datetime
import unittest

from src.authentication.authentication import Authentication

class TestAuthentication(unittest.TestCase):
    """Classe que testa a classe Authentication."""
    def __init__(self, *args, **kwargs):
        super(TestAuthentication, self).__init__(*args, **kwargs)
        self.email = 'email.test@test.com'
        self.password = 'password123'

    def test_constructor(self):
        """Testa o construtor da classe Authentication."""
        auth = Authentication()
        self.assertIsNone(auth.uid)

    def test_create_user(self):
        """Testa o método create_user."""
        auth = Authentication()
        auth.create_user(self.email, self.password)
        self.assertIsNotNone(auth.uid)
        auth.delete_user(auth.uid)

    def test_get_user(self):
        """Testa o método get_user."""
        auth = Authentication()
        auth.create_user(self.email, self.password)
        user = auth.get_user_by_email(self.email)
        self.assertEqual(user.uid, auth.uid)
        auth.delete_user(auth.uid)

    def test_delete_user(self):
        """Testa o método delete_user."""
        auth = Authentication()
        auth.create_user(self.email, self.password)
        auth.delete_user(auth.uid)
        self.assertIsNone(auth.uid)

    def test_authenticate(self):
        """Testa o método authenticate."""
        auth = Authentication()
        auth.create_user(self.email, self.password)
        self.assertTrue(auth.authenticate(self.email, self.password))
        auth.delete_user(auth.uid)
        self.assertFalse(auth.authenticate(self.email, self.password))

    def test_update_user_password(self):
        """Testa o método update_user_password."""
        auth = Authentication()
        auth.create_user(self.email, self.password)
        auth.update_user_password(auth.uid, self.password)
        self.assertTrue(auth.authenticate(self.email, self.password))
        auth.delete_user(auth.uid)

    def test_update_user_email(self):
        """Testa o método update_user_email."""
        auth = Authentication()
        auth.create_user(self.email, self.password)
        new_email = 'new'+ self.email
        auth.update_user_email(auth.uid, new_email)

    def test_get_all_users(self):
        """Testa o método get_all_users."""
        auth = Authentication()
        auth.create_user(self.email, self.password)
        users = auth.get_all_users()
        self.assertTrue(len(users.users) > 0)
        auth.delete_user(auth.uid)

if __name__ == '__main__':
    unittest.main()
