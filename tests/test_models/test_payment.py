import unittest
from datetime import date

from src.models.Payment import Payment


class TestPayment(unittest.TestCase):
    def test_constructor(self) -> None:
        """
        Testa o construtor da classe Payment conferindo se os
        atributos foram definidos corretamente.
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

    def test_payment_date_setter_limitation(self) -> None:
        """
        Testa o setter da classe Payment conferindo se
        ele não permite que o atributo payment_date seja
        menor que o atributo reference_date.
        """
        payment = Payment(
            value=10.0,
            payment_date=date(2021, 1, 2),
            reference_date=date(2021, 1, 2),
        )
        with self.assertRaises(ValueError):
            payment.payment_date = date(2021, 1, 1)
        self.assertEqual(payment.payment_date, date(2021, 1, 2))

    def test_value_setter_limitation(self) -> None:
        """
        Testa o setter da classe Payment conferindo se ele não
        permite que o atributo value seja menor que zero.
        """
        payment = Payment(
            value=10.0,
            payment_date=date(2021, 1, 2),
            reference_date=date(2021, 1, 2),
        )
        with self.assertRaises(ValueError):
            payment.value = -1.0
        self.assertEqual(payment.value, 10.0)


if __name__ == "__main__":
    unittest.main()
