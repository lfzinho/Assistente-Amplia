import unittest

from . import init_path
from src.models.PaymentMethod import PaymentMethod


class TestPaymentMethod(unittest.TestCase):
    def test_init_is_abstract(self) -> None:
        self.assertIn('__init__', PaymentMethod.__abstractmethods__)

    def test_get_information_is_abstract(self) -> None:
        self.assertIn(
            'get_information',
            PaymentMethod.__abstractmethods__
        )

    def test_is_abstract(self) -> None:
        self.assertTrue(PaymentMethod.__abstractmethods__)


if __name__ == '__main__':
    unittest.main()
