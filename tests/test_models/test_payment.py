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

    def test_getters(self) -> None:
        """
        Testa os getters da classe Payment conferindo se
        eles retornam os valores corretos.
        """
        payment = Payment(
            value=10.0,
            payment_date=date(2021, 1, 1),
            reference_date=date(2021, 1, 1),
        )
        self.assertEqual(payment.value, 10.0)
        self.assertEqual(payment.payment_date, date(2021, 1, 1))
        self.assertEqual(payment.reference_date, date(2021, 1, 1))

    def test_setters(self) -> None:
        """
        Testa os setters da classe Payment conferindo se
        eles atribuem os valores corretos.
        """
        payment = Payment(
            value=10.0,
            payment_date=date(2021, 1, 1),
            reference_date=date(2021, 1, 1),
        )
        payment.value = 20.0
        payment.payment_date = date(2021, 1, 2)
        payment.reference_date = date(2021, 1, 3)
        self.assertEqual(payment.value, 20.0)
        self.assertEqual(payment.payment_date, date(2021, 1, 2))
        self.assertEqual(payment.reference_date, date(2021, 1, 3))


if __name__ == "__main__":
    unittest.main()
