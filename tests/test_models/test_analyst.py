"""Módulo de testes do módulo src.models.Analyst
"""
import unittest
from abc import ABC

from . import init_path
from src.models.BankAccount import BankAccount
from src.models.PaymentMethod import PaymentMethod
from src.models.Pix import Pix
from src.models.Analyst import Analyst


class TestAnalyst(unittest.TestCase):
    """Classe que testa a classe Analyst"""
    def test_constructor(self) -> None:
        """
        Testa o construtor da classe Analyst conferindo se os
        atributos foram setados corretamente.
        """
        analyst = Analyst(
            name='João',
            email='joaosilva@gmail.com',
            cpf='123.456.789-00',
            address='Rua 1, 123',
            payment_method=Pix(key='12345678900', type_='cpf'),
            birth_date='1990-01-01',
            admission_date='2021-01-01',
            occupation_area='Administrativo Financeiro',
            exit_date='2021-02-01'
        )
        self.assertIsInstance(analyst, Analyst)

    def test_constructor_nones(self) -> None:
        """
        Testa o construtor da classe Analyst conferindo se os
        atributos foram setados corretamente.
        """
        analyst = Analyst(
            name='João',
            email='joaosilva@gmail.com',
            cpf='123.456.789-00',
            address='Rua 1, 123',
            payment_method=Pix(key='12345678900', type_='cpf'),
            birth_date='1990-01-01',
            admission_date='2021-01-01',
            occupation_area='Administrativo Financeiro',
        )
        self.assertIsInstance(analyst, Analyst)
        self.assertEqual(analyst.exit_date, None)

    def test_getters(self) -> None:
        """Testa os getters da classe Analyst"""
        analyst = Analyst(
            name='João',
            email='joaosilva@gmail.com',
            cpf='123.456.789-00',
            address='Rua 1, 123',
            payment_method=Pix(key='12345678900', type_='cpf'),
            birth_date='1990-01-01',
            admission_date='2021-01-01',
            occupation_area='Administrativo Financeiro',
            exit_date='2021-02-01',
        )
        self.assertEqual(analyst.name, 'João')
        self.assertEqual(analyst.email, 'joaosilva@gmail.com')
        self.assertEqual(analyst.cpf, '123.456.789-00')
        self.assertEqual(analyst.address, 'Rua 1, 123')
        self.assertIsInstance(analyst.payment_method, PaymentMethod)
        self.assertEqual(analyst.birth_date, '1990-01-01')
        self.assertEqual(analyst.admission_date, '2021-01-01')
        self.assertEqual(analyst.occupation_area, 'Administrativo Financeiro')
        self.assertEqual(analyst.exit_date, '2021-02-01')

    def test_setters(self) -> None:
        """Testa os setters da classe Analyst"""
        # Instancia a classe com um conjunto A de parâmetros
        analyst = Analyst(
            name='João',
            email='joaosilva@gmail.com',
            cpf='123.456.789-00',
            address='Rua 1, 123',
            payment_method=Pix(key='12345678900', type_='cpf'),
            birth_date='1990-01-01',
            admission_date='2021-01-01',
            occupation_area='Administrativo Financeiro',
            exit_date='2021-02-01'
        )
        # Seta os atributos da classe para um conjunto B de parâmetros
        analyst.name = 'Maria'
        analyst.email = 'mariasouza@hotmail.com'
        analyst.cpf = '987.654.321-00'
        analyst.address = 'Rua 2, 321'
        analyst.payment_method = BankAccount(
            bank='Banco 1',
            agency=123,
            account_number=12345
        )
        analyst.birth_date = '1990-02-02'
        analyst.admission_date = '2021-02-01'
        analyst.occupation_area = 'Recursos Humanos'
        analyst.exit_date = '2021-03-01'
        # Testa se os atributos da classe correspondem ao conjunto B de
        # parâmetros
        self.assertEqual(analyst.name, 'Maria')
        self.assertEqual(analyst.email, 'mariasouza@hotmail.com')
        self.assertEqual(analyst.cpf, '987.654.321-00')
        self.assertEqual(analyst.address, 'Rua 2, 321')
        self.assertIsInstance(analyst.payment_method, BankAccount)
        self.assertEqual(analyst.birth_date, '1990-02-02')
        self.assertEqual(analyst.admission_date, '2021-02-01')
        self.assertEqual(analyst.occupation_area, 'Recursos Humanos')
        self.assertEqual(analyst.exit_date, '2021-03-01')

    def test_occupation_area_literal_init(self) -> None:
        """
        Testa se o Analyst.__init__(...) levanta ValueError ao receber
        um valor inválido para o atributo 'occupation_area'
        """
        with self.assertRaises(ValueError):
            analyst = Analyst(
                name='João',
                email='joaosilva@gmail.com',
                cpf='123.456.789-00',
                address='Rua 1, 123',
                payment_method=Pix(key='12345678900', type_='cpf'),
                birth_date='1990-01-01',
                admission_date='2021-01-01',
                occupation_area='invalid_value',
                exit_date='2021-02-01'
            )

    def test_occupation_area_literal_setter(self) -> None:
        """
        Testa se o Analyst.occupation_area.setter levanta ValueError ao
        receber um valor inválido
        """
        analyst = Analyst(
            name='João',
            email='joaosilva@gmail.com',
            cpf='123.456.789-00',
            address='Rua 1, 123',
            payment_method=Pix(key='12345678900', type_='cpf'),
            birth_date='1990-01-01',
            admission_date='2021-01-01',
            occupation_area='Administrativo Financeiro',
            exit_date='2021-02-01'
        )

        with self.assertRaises(ValueError):
            analyst.occupation_area = 'invalid_value'
