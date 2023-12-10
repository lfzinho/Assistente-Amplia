import unittest

from . import init_path
from src.models.PaymentEventListener import PaymentEventListener


class TestPaymentEventListener(unittest.TestCase):
    """Classe responsável por testar a classe PaymentEventListener."""
    def test_constructor(self) -> None:
        """
        Testa o construtor da classe PaymentEventListener conferindo se os
        atributos foram setados corretamente.
        """
        payment_event_listener = PaymentEventListener()
        self.assertIsInstance(payment_event_listener, PaymentEventListener)
        self.assertEqual(payment_event_listener.listeners, [])


if __name__ == '__main__':
    unittest.main()
