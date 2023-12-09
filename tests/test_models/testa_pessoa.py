import unittest
from abc import ABC

from . import init_path
from src.models.ContaBancaria import ContaBancaria
from src.models.Pix import Pix
from src.models.Pessoa import Pessoa


class TestaPessoa(unittest.TestCase):

    def testa_pessoa(self) -> None:
        """
        Testa o construtor da classe Pessoa conferindo se os
        atributos foram setados corretamente.
        """
        pessoa = Pessoa(
            nome='João',
            data_nascimento='1990-01-01',
            cpf='123.456.789-00',
            endereco='Rua 1, 123',
            metodo_pagamento=Pix(chave='12345678900', tipo='cpf')
        )
        self.assertIsInstance(pessoa, Pessoa)
        self.assertEqual(pessoa._nome, 'João')
        self.assertEqual(pessoa._data_nascimento, '1990-01-01')
        self.assertEqual(pessoa._cpf, '123.456.789-00')
        self.assertEqual(pessoa._endereco, 'Rua 1, 123')

    def testa_getters(self) -> None:
        """Testa os getters da classe Pessoa."""
        pessoa = Pessoa(
            nome='João',
            data_nascimento='1990-01-01',
            cpf='123.456.789-00',
            endereco='Rua 1, 123',
            metodo_pagamento=Pix(chave='12345678900', tipo='cpf')
        )
        self.assertEqual(pessoa._nome, 'João')
        self.assertEqual(pessoa._data_nascimento, '1990-01-01')
        self.assertEqual(pessoa._cpf, '123.456.789-00')
        self.assertEqual(pessoa._endereco, 'Rua 1, 123')
        self.assertEqual(
            pessoa._metodo_pagamento.visualizar_informacoes(),
            'Chave: 12345678900\nTipo: cpf'
        )

    def testa_setters(self) -> None:
        """Testa os setters da classe Pessoa."""
        pessoa = Pessoa(
            nome='João',
            data_nascimento='1990-01-01',
            cpf='123.456.789-00',
            endereco='Rua 1, 123',
            metodo_pagamento=Pix(chave='12345678900', tipo='cpf')
        )
        pessoa.nome = 'Maria'
        pessoa.data_nascimento = '1990-02-02'
        pessoa.cpf = '987.654.321-00'
        pessoa.endereco = 'Rua 2, 321'
        pessoa.metodo_pagamento = ContaBancaria(
            banco='Banco 1', agencia='123', nro_conta='123456'
        )
        self.assertEqual(pessoa._nome, 'Maria')
        self.assertEqual(pessoa._data_nascimento, '1990-02-02')
        self.assertEqual(pessoa._cpf, '987.654.321-00')
        self.assertEqual(pessoa._endereco, 'Rua 2, 321')
        self.assertEqual(
            pessoa._metodo_pagamento.visualizar_informacoes(),
            'Banco: Banco 1\nAgência: 123\nNúmero da conta: 123456'
        )

    def testa_eh_abstract(self) -> None:
        """Testa se a classe Pessoa é abstrata."""
        self.assertTrue(issubclass(Pessoa, ABC))


if __name__ == '__main__':
    unittest.main()
