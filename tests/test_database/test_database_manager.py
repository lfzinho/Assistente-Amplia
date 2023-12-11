import unittest

from src.database.database import DatabaseManager


class TestDatabaseManager(unittest.TestCase):
    """Classe que testa a classe DatabaseManager."""

    def test_singleton(self):
        """Testa se a classe é um singleton."""
        dbm1 = DatabaseManager.instance()
        dbm2 = DatabaseManager.instance()
        self.assertEqual(dbm1, dbm2)

    def test_add(self):
        """Testa o método add."""
        dbm = DatabaseManager.instance()
        dbm.add('test', {'test': 'test'})
        index = dbm.get_by_id('test', 'index')['index'] - 1
        index = str(index)
        self.assertIsInstance(dbm.get_by_id('test', index), dict)
        dbm.delete('test', index)

    def test_get_all(self):
        """Testa o método get_all."""
        dbm = DatabaseManager.instance()
        dbm.add('test', {'test': 'test'})
        index = dbm.get_by_id('test', 'index')['index'] - 1
        index = str(index)
        self.assertIsInstance(dbm.get_all('test'), dict)
        dbm.delete('test', index)

    def test_get_all_keys(self):
        """Testa o método get_all_keys."""
        dbm = DatabaseManager.instance()
        dbm.add('test', {'test': 'test'})
        index = dbm.get_by_id('test', 'index')['index'] - 1
        index = str(index)
        self.assertIsInstance(dbm.get_all_keys('test'), list)
        dbm.delete('test', index)

    def test_get_by_id(self):
        """Testa o método get_by_id."""
        dbm = DatabaseManager.instance()
        dbm.add('test', {'test': 'test'})
        index = dbm.get_by_id('test', 'index')['index'] - 1
        index = str(index)
        self.assertIsInstance(dbm.get_by_id('test', index), dict)
        dbm.delete('test', index)

    def test_update(self):
        """Testa o método update."""
        dbm = DatabaseManager.instance()
        dbm.add('test', {'test': 'test'})
        index = dbm.get_by_id('test', 'index')['index'] - 1
        index = str(index)
        self.assertEqual(dbm.get_by_id('test', index), {'test': 'test'})
        dbm.update('test', index, {'test': 'test_updated'})
        self.assertEqual(dbm.get_by_id('test', index), {'test': 'test_updated'})
        dbm.delete('test', index)

    def test_delete(self):
        """Testa o método delete."""
        dbm = DatabaseManager.instance()
        dbm.add('test', {'test': 'test'})
        index = dbm.get_by_id('test', 'index')['index'] - 1
        index = str(index)
        self.assertIsInstance(dbm.get_by_id('test', index), dict)
        self.assertEqual(dbm.delete('test', index), True)
        self.assertEqual(dbm.get_by_id('test', index), None)


if __name__ == '__main__':
    unittest.main()
