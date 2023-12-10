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

    def test_add(self):
        """Testa o método add"""
        dbm = DatabaseManager.instance()
        dbm.add('test', {'test': 'test'})
        index = dbm.get_by_id('test', 'index')['index'] - 1
        index = str(index)
        self.assertIsInstance(dbm.get_by_id('test', index), dict)
        dbm.delete('test', index)

    def test_get_all(self):
        """Testa o método get_all"""
        dbm = DatabaseManager.instance()
        dbm.add('test', {'test': 'test'})
        index = dbm.get_by_id('test', 'index')['index'] - 1
        index = str(index)
        self.assertIsInstance(dbm.get_all('test'), dict)
        dbm.delete('test', index)

if __name__ == '__main__':
    unittest.main()
