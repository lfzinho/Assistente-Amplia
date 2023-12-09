import unittest
from abc import ABC

from . import init_path
from src.models.BankAccount import BankAccount
from src.models.PaymentMethod import PaymentMethod
from src.models.Pix import Pix
from src.models.Person import Person


class TestPerson(unittest.TestCase):
    """Classe que testa a classe Person."""
    def test_constructor(self) -> None:
        """
        Testa o construtor da classe Person conferindo se os
        atributos foram setados corretamente.
        """
        person = Person(
            name='João',
            email='joaosilva@gmail.com',
            cpf='123.456.789-00',
            address='Rua 1, 123',
            payment_method=Pix(key='12345678900', type_='cpf'),
            birth_date='1990-01-01',
            admission_date='2021-01-01',
            exit_date='2021-02-01'
        )
        self.assertIsInstance(person, Person)
        self.assertEqual(person.name, 'João')
        self.assertEqual(person.email, 'joaosilva@gmail.com')
        self.assertEqual(person.cpf, '123.456.789-00')
        self.assertEqual(person.address, 'Rua 1, 123')
        self.assertIsInstance(person.payment_method, PaymentMethod)
        self.assertEqual(person.birth_date, '1990-01-01')
        self.assertEqual(person.admission_date, '2021-01-01')
        self.assertEqual(person.exit_date, '2021-02-01')

    def test_constructor_nones(self) -> None:
        """
        Testa o construtor da classe Person conferindo se os
        atributos foram setados corretamente.
        """
        person = Person(
            name='João',
            email='joaosilva@gmail.com',
            cpf='123.456.789-00',
            address='Rua 1, 123',
            payment_method=Pix(key='12345678900', type_='cpf'),
            birth_date='1990-01-01',
            admission_date='2021-01-01'
        )
        self.assertIsInstance(person, Person)
        self.assertEqual(person.exit_date, None)


if __name__ == '__main__':
    unittest.main()
