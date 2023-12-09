import unittest

from . import init_path
from src.models.Cash import Cash


class TestCash(unittest.TestCase):
    def test_constructor(self) -> None:
        """
        Testa o construtor da classe Cash conferindo se os
        atributos foram setados corretamente.
        """
        cash = Cash(
            saved_amount=10.0
        )
        self.assertIsInstance(cash, Cash)
        self.assertEqual(cash.saved_amount, 10.0)

    def test_make_payment_return_4(self) -> None:
        """
        Testa o método make_payment da classe Cash conferindo se
        ele retorna 4.0 ao inserir um amount de 6.0 em um saldo de 10.0.
        """
        cash = Cash(
            saved_amount=10.0
        )
        cash.make_payment(amount=6.0)
        self.assertEqual(cash.saved_amount, 4.0)

    def test_make_payment_subtraction(self) -> None:
        """
        Testa o método make_payment da classe Cash conferindo se
        a subtração do atributo saved_amount foi feita corretamente.
        """
        cash = Cash(
            saved_amount=10.0
        )
        cash.make_payment(amount=6.0)
        self.assertEqual(cash.saved_amount, 4.0)
        cash.make_payment(amount=3.0)
        self.assertEqual(cash.saved_amount, 1.0)

    def test_make_payment_dont_allow_negative_values(self) -> None:
        """
        Testa o método make_payment da classe Cash conferindo se
        ele não permite valores negativos.
        """
        cash = Cash(
            saved_amount=10.0
        )
        with self.assertRaises(ValueError):
            cash.make_payment(amount=-6.0)
        with self.assertRaises(ValueError):
            cash.make_payment(amount=0.0)
        self.assertEqual(cash.saved_amount, 10.0)

    def test_make_payment_greater_than_saved_amount(self) -> None:
        """
        Testa o método make_payment da classe Cash conferindo se
        ele não permite valores maiores que o saldo.
        """
        cash = Cash(
            saved_amount=10.0
        )
        with self.assertRaises(ValueError):
            cash.make_payment(amount=11.0)
        self.assertEqual(cash.saved_amount, 10.0)


if __name__ == '__main__':
    unittest.main()
