import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

import datetime
import unittest

from src.database.database import DatabaseManager

class TestDatabaseManager(unittest.TestCase):
    """Classe que testa a classe DatabaseManager"""

    def test_singleton(self):
        """Testa se a classe é um singleton"""
        dbm1 = DatabaseManager.instance()
        dbm2 = DatabaseManager.instance()
        self.assertEqual(dbm1, dbm2)

if __name__ == '__main__':
    unittest.main()
