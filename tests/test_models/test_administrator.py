import unittest
from datetime import date

from src.models.Pix import Pix
from src.models.Administrator import Administrator


class TestAdministrator(unittest.TestCase):
    """Classe que testa a classe Administrator."""
    def test_constructor(self) -> None:
        """
        Testa o construtor da classe Administrator conferindo se os
        atributos foram definidos corretamente.
        """
        director = Administrator(
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
        self.assertIsInstance(director, Administrator)


if __name__ == '__main__':
    unittest.main()
