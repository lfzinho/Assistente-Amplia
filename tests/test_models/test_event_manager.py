import unittest

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

    def test_remove_listener(self) -> None:
        """
        Testa o método remove_listener da classe EventManager conferindo se os
        atributos foram setados corretamente.
        """
        event_manager = EventManager()
        payment_event_listener = PaymentEventListener()
        event_manager.add_listener(payment_event_listener)
        event_manager.remove_listener(payment_event_listener)
        self.assertEqual(event_manager.listeners, [])

    # def test_notify(self) -> None:
    #     """
    #     Testa o método notify da classe EventManager conferindo se os
    #     atributos foram setados corretamente.
    #     """
    #     event_manager = EventManager()
    #     payment_event_listener = PaymentEventListener()
    #     event_manager.add_listener(payment_event_listener)
    #     event_manager.notify('payment')
    #     self.assertEqual(payment_event_listener.event, 'payment')

    def test_notify_without_listeners(self) -> None:
        """
        Testa o método notify da classe EventManager conferindo se os
        atributos foram setados corretamente.
        """
        event_manager = EventManager()
        event_manager.notify('payment')
        self.assertEqual(event_manager.listeners, [])

if __name__ == '__main__':
    unittest.main()
