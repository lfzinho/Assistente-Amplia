import unittest

from . import init_path
from src.models.EventManager import EventManager
from src.models.PaymentEventListener import PaymentEventListener


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

    def test_add_listener(self) -> None:
        """
        Testa o método add_listener da classe EventManager conferindo se os
        atributos foram setados corretamente.
        """
        event_manager = EventManager()
        payment_event_listener = PaymentEventListener()
        event_manager.add_listener(payment_event_listener)
        self.assertEqual(event_manager.listeners, [payment_event_listener])

if __name__ == '__main__':
    unittest.main()
