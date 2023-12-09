import unittest

from . import init_path
from src.models.ContaBancaria import ContaBancaria
from src.models.Pessoa import Pessoa
from src.models.Pix import Pix
from src.models.Professor import Professor


class TestaProfessor(unittest.TestCase):
    def testa_heranca_pessoa(self) -> None:
        """Testa se a classe Aluno herda de Pessoa."""
        self.assertTrue(issubclass(Professor, Pessoa))

    def testa_construtor(self) -> None:
        """Testa se o construtor da classe Professor funciona."""
        professor = Professor(
            nome='João',
            data_nascimento='1999-01-01',
            cpf='12345678901',
            endereco='Rua 1',
            metodo_pagamento=Pix(
                chave='12345678901',
                tipo='cpf'
            ),
            salario=1000.0
        )
        # testa se a instância é da classe Professor
        self.assertIsInstance(professor, Professor)
        self.assertIsInstance(professor, Pessoa)
        # testa se os atributos foram definidos corretamente
        self.assertEqual(professor.nome, 'João')
        self.assertEqual(professor.data_nascimento, '1999-01-01')
        self.assertEqual(professor.cpf, '12345678901')
        self.assertEqual(professor.endereco, 'Rua 1')
        self.assertIsInstance(professor.metodo_pagamento, Pix)
        self.assertEqual(professor._salario, 1000.0)

    def testa_getter_salario(self) -> None:
        """Testa se o getter do atributo salario funciona."""
        professor = Professor(
            nome='João',
            data_nascimento='1999-01-01',
            cpf='12345678901',
            endereco='Rua 1',
            metodo_pagamento=Pix(
                chave='12345678901',
                tipo='cpf'
            ),
            salario=1000.0
        )
        self.assertEqual(professor.salario, 1000.0)

    def testa_setter_salario(self) -> None:
        """Testa se o setter do atributo salario funciona"""
        professor = Professor(
            nome='João',
            data_nascimento='1999-01-01',
            cpf='12345678901',
            endereco='Rua 1',
            metodo_pagamento=Pix(
                chave='12345678901',
                tipo='cpf'
            ),
            salario=1000.0
        )
        professor.salario = 2000.0
        self.assertEqual(professor.salario, 2000.0)

    def testa_setter_salario_negativo(self) -> None:
        """Testa se o setter do atributo salario funciona"""
        professor = Professor(
            nome='João',
            data_nascimento='1999-01-01',
            cpf='12345678901',
            endereco='Rua 1',
            metodo_pagamento=Pix(
                chave='12345678901',
                tipo='cpf'
            ),
            salario=1000.0
        )
        with self.assertRaises(ValueError):
            professor.salario = -2000.0


if __name__ == '__main__':
    unittest.main()