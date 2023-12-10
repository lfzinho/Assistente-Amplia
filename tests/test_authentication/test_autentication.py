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

if __name__ == '__main__':
    unittest.main()
