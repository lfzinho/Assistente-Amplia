"""
Módulo de testes do módulo src.models.Person.

Os métodos de teste de construtor, getters e setters
da classe Person estão comentados por se tratar de
uma classe abstrata. Eles são apenas "resíduos" do TDD.
"""
import unittest
from abc import ABC

from src.models.BankAccount import BankAccount
from src.models.PaymentMethod import PaymentMethod
from src.models.Pix import Pix
from src.models.Person import Person


class TestPerson(unittest.TestCase):
    # """Classe que testa a classe Person."""
    # def test_constructor(self) -> None:
    #     """
    #     Testa o construtor da classe Person conferindo se os
    #     atributos foram setados corretamente.
    #     """
    #     person = Person(
    #         name='João',
    #         email='joaosilva@gmail.com',
    #         cpf='123.456.789-00',
    #         address='Rua 1, 123',
    #         payment_method=Pix(key='12345678900', type_='cpf'),
    #         birth_date=date(year=1990, month=1, day=1),
    #         admission_date=date(year=2021, month=1, day=1),
    #         exit_date=date(year=2022, month=1, day=1)
    #     )
    #     self.assertIsInstance(person, Person)

    # def test_constructor_nones(self) -> None:
    #     """
    #     Testa o construtor da classe Person conferindo se os
    #     atributos foram setados corretamente.
    #     """
    #     person = Person(
    #         name='João',
    #         email='joaosilva@gmail.com',
    #         cpf='123.456.789-00',
    #         address='Rua 1, 123',
    #         payment_method=Pix(key='12345678900', type_='cpf'),
    #         birth_date=date(year=1990, month=1, day=1),
    #         admission_date=date(year=2021, month=1, day=1)
    #     )
    #     self.assertIsInstance(person, Person)
    #     self.assertEqual(person.exit_date, None)

    # def test_getters(self) -> None:
    #     """Testa os getters da classe Person."""
    #     person = Person(
    #         name='João',
    #         email='joaosilva@gmail.com',
    #         cpf='123.456.789-00',
    #         address='Rua 1, 123',
    #         payment_method=Pix(key='12345678900', type_='cpf'),
    #         birth_date=date(year=1990, month=1, day=1),
    #         admission_date=date(year=2021, month=1, day=1),
    #         exit_date=date(year=2022, month=1, day=1)
    #     )
    #     self.assertEqual(person.name, 'João')
    #     self.assertEqual(person.email, 'joaosilva@gmail.com')
    #     self.assertEqual(person.cpf, '123.456.789-00')
    #     self.assertEqual(person.address, 'Rua 1, 123')
    #     self.assertIsInstance(person.payment_method, Pix)
    #     self.assertEqual(person.birth_date, date(year=1990, month=1, day=1))
    #     self.assertEqual(person.admission_date, date(year=2021, month=1, day=1))
    #     self.assertEqual(person.exit_date, date(year=2022, month=1, day=1))

    # def test_setters(self) -> None:
    #     """Testa os setters da classe Person."""
    #     person = Person(
    #         name='João',
    #         email='joaosilva@gmail.com',
    #         cpf='123.456.789-00',
    #         address='Rua 1, 123',
    #         payment_method=Pix(key='12345678900', type_='cpf'),
    #         birth_date=date(year=1990, month=1, day=1),
    #         admission_date=date(year=2021, month=1, day=1),
    #         exit_date=date(year=2022, month=1, day=1)
    #     )
    #     person.name = 'Maria'
    #     person.email = 'mariasouza@hotmail.com'
    #     person.cpf = '987.654.321-00'
    #     person.address = 'Rua 2, 321'
    #     person.payment_method = BankAccount(
    #         bank='Banco 1',
    #         agency=123,
    #         account_number=12345
    #     )
    #     person.birth_date = '1990-02-02'
    #     person.admission_date = date(year=2022, month=1, day=1)
    #     person.exit_date = '2021-03-01'
    #     self.assertEqual(person.name, 'Maria')
    #     self.assertEqual(person.email, 'mariasouza@hotmail.com')
    #     self.assertEqual(person.cpf, '987.654.321-00')
    #     self.assertEqual(person.address, 'Rua 2, 321')
    #     self.assertIsInstance(person.payment_method, BankAccount)
    #     self.assertEqual(person.birth_date, '1990-02-02')
    #     self.assertEqual(person.admission_date, date(year=2022, month=1, day=1))
    #     self.assertEqual(person.exit_date, '2021-03-01')

    def test_is_abstract(self) -> None:
        """Testa se a classe Person é abstrata."""
        self.assertTrue(ABC.__subclasshook__(Person))


if __name__ == '__main__':
    unittest.main()
