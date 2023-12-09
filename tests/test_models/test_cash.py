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
