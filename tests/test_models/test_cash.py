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
        a subtração do atributo saved_amount foi feita corretamente.
        """
        cash = Cash(
            saved_amount=10.0
        )
        cash.make_payment(amount=6.0)
        self.assertEqual(cash.saved_amount, 4.0)


if __name__ == '__main__':
    unittest.main()
