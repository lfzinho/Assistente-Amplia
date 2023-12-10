import unittest
from abc import ABC

from src.models.Beneficiary import Beneficiary
from src.models.Person import Person
from src.models.Pix import Pix


class TestBeneficiary(unittest.TestCase):
    # def test_constructor(self) -> None:
    #     """
    #     Testa o construtor da classe Beneficiary conferindo se os
    #     atributos foram definidos corretamente.
    #     """
    #     beneficiary = Beneficiary(
    #         transport_cost=10.0,
    #         transport_description='Uber'
    #     )
    #     self.assertIsInstance(beneficiary, Beneficiary)
    #     self.assertEqual(beneficiary.transport_cost, 10.0)
    #     self.assertEqual(beneficiary.transport_description, 'Uber')

    # def test_constructor(self) -> None:
    #     """
    #     Testa o construtor da classe Beneficiary conferindo se os
    #     atributos foram definidos corretamente.
    #     """
    #     beneficiary = Beneficiary(
    #         name='João',
    #         email='joaosilva@gmail.com',
    #         cpf='123.456.789-00',
    #         address='Rua 1, 123',
    #         payment_method=Pix(key='12345678900', type_='cpf'),
    #         birth_date='1990-01-01',
    #         admission_date='2021-01-01',
    #         exit_date='2021-02-01',
    #         transport_cost=10.0,
    #         transport_description='Uber'
    #     )
    #     self.assertIsInstance(beneficiary, Beneficiary)
    #     self.assertEqual(beneficiary.transport_cost, 10.0)
    #     self.assertEqual(beneficiary.transport_description, 'Uber')

    def test_inheritance(self) -> None:
        """Testa se Beneficiary herda de Person."""
        self.assertTrue(issubclass(Beneficiary, Person))

    def test_is_abstract(self) -> None:
        """Testa se Beneficiary é uma classe abstrata."""
        self.assertTrue(issubclass(Beneficiary, ABC))

    def test_is_constructor_abstract(self) -> None:
        """Testa se o construtor de Beneficiary é abstrato."""
        with self.assertRaises(TypeError):
            Beneficiary()

if __name__ == '__main__':
    unittest.main()
