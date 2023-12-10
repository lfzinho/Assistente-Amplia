import unittest

from src.models.BankAccount import BankAccount
from src.models.PaymentMethod import PaymentMethod


class TestBankAccount(unittest.TestCase):
    """Classe que testa a classe BankAccount."""
    def test_constructor(self) -> None:
        """
        Testa o construtor da classe BankAccount conferindo se os
        atributos foram setados corretamente.
        """
        bank_account = BankAccount('Itaú', '123456', '12345678')
        self.assertIsInstance(bank_account, BankAccount)

        self.assertEqual(bank_account._agency, '123456')
        self.assertEqual(bank_account._account_number, '12345678')
        self.assertEqual(bank_account._bank, 'Itaú')

    def test_inheritance_payment_method(self) -> None:
        """
        Testa se a classe BankAccount herda de PaymentMethod.
        """
        self.assertTrue(issubclass(BankAccount, PaymentMethod))

    def test_return_get_information(self) -> None:
        """
        Testa se o método `get_information`
        retorna as informações corretas.
        """
        bank_account = BankAccount('Itaú', '123456', '12345678')
        self.assertEqual(
            bank_account.get_information(),
            'Banco: Itaú\nAgência: 123456\nNúmero da conta: 12345678'
        )

    def test_getters(self) -> None:
        """Testa se os getters funcionam corretamente."""
        bank_account = BankAccount('Itaú', '123456', '12345678')
        self.assertEqual(bank_account.bank, 'Itaú')
        self.assertEqual(bank_account.agency, '123456')
        self.assertEqual(bank_account.account_number, '12345678')

    def test_setters(self) -> None:
        """Testa se os setters funcionam corretamente."""
        bank_account = BankAccount('Itaú', '123456', '12345678')
        bank_account.bank = 'Bradesco'
        bank_account.agency = '654321'
        bank_account.account_number = '87654321'
        self.assertEqual(bank_account.bank, 'Bradesco')
        self.assertEqual(bank_account.agency, '654321')
        self.assertEqual(bank_account.account_number, '87654321')
