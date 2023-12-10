import unittest
from datetime import date

from src.models.Pix import Pix
from src.models.Director import Director

class TestDirector(unittest.TestCase):
    """Classe que testa a classe Director."""
    def test_constructor(self) -> None:
        """
        Testa o construtor da classe Director conferindo se os
        atributos foram setados corretamente.
        """
        director = Director(
            name='João',
            email='joaosilva@gmail.com',
            cpf='123.456.789-00',
            address='Rua 1, 123',
            payment_method=Pix(key='12345678900', type_='cpf'),
            birth_date=date(year=1990, month=1, day=1),
            admission_date=date(year=2021, month=1, day=1),
            occupation_area='Administrativo Financeiro',
            office_admission_date=date(year=2021, month=1, day=1),
            office_exit_date=date(year=2022, month=1, day=1),
            exit_date=date(year=2022, month=1, day=1),
        )
        self.assertIsInstance(director, Director)

    def test_constructor_nones(self) -> None:
        """
        Testa o construtor da classe Director conferindo se os
        atributos foram setados corretamente.
        """
        director = Director(
            name='João',
            email='joaosilva@gmail.com',
            cpf='123.456.789-00',
            address='Rua 1, 123',
            payment_method=Pix(key='12345678900', type_='cpf'),
            birth_date=date(year=1990, month=1, day=1),
            admission_date=date(year=2021, month=1, day=1),
            occupation_area='Administrativo Financeiro',
            office_admission_date=date(year=2021, month=1, day=1)
        )
        self.assertIsInstance(director, Director)
        self.assertEqual(director.office_exit_date, None)

    def test_constructor_inconsistent_admission(self) -> None:
        """
        Testa o construtor da classe Director conferindo se é levantado
        erro ao passar datas inconsistentes.
        """
        with self.assertRaises(ValueError):
            director = Director(
                name='João',
                email='joaosilva@gmail.com',
                cpf='123.456.789-00',
                address='Rua 1, 123',
                payment_method=Pix(key='12345678900', type_='cpf'),
                birth_date=date(year=1990, month=1, day=1),
                admission_date=date(year=2022, month=1, day=1),
                occupation_area='Administrativo Financeiro',
                office_admission_date=date(year=2021, month=1, day=1),
            )

    def test_constructor_inconsistent_exit(self) -> None:
        """
        Testa o construtor da classe Director conferindo se é levantado
        erro ao passar datas inconsistentes.
        """
        with self.assertRaises(ValueError):
            director = Director(
                name='João',
                email='joaosilva@gmail.com',
                cpf='123.456.789-00',
                address='Rua 1, 123',
                payment_method=Pix(key='12345678900', type_='cpf'),
                birth_date=date(year=1990, month=1, day=1),
                admission_date=date(year=2021, month=1, day=1),
                occupation_area='Administrativo Financeiro',
                office_admission_date=date(year=2023, month=1, day=1),
                office_exit_date=date(year=2022, month=1, day=1),
            )

if __name__ == '__main__':
    unittest.main()
