import unittest
from datetime import date

from . import init_path
from src.models.Payment import Payment


class TestPayment(unittest.TestCase):
    def test_constructor(self) -> None:
        """
        Testa o construtor da classe Payment conferindo se os
        atributos foram setados corretamente.
        """
        payment = Payment(
            value=10.0,
            payment_date=date(2021, 1, 1),
            reference_date=date(2021, 1, 1),
        )
        self.assertIsInstance(payment, Payment)
        self.assertEqual(payment.value, 10.0)
        self.assertEqual(payment.payment_date, date(2021, 1, 1))
        self.assertEqual(payment.reference_date, date(2021, 1, 1))
