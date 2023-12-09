import unittest

from . import init_path
from src.models.EventManager import EventManager


class TestEventManager(unittest.TestCase):
    """Classe responsável por testar a classe EventManager."""
    def test_constructor(self) -> None:
        """
        Testa o construtor da classe EventManager conferindo se os
        atributos foram setados corretamente.
        """
        event_manager = EventManager()
        self.assertIsInstance(event_manager, EventManager)
        self.assertEqual(event_manager.listeners, [])


if __name__ == '__main__':
    unittest.main()
