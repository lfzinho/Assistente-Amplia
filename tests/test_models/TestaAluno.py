import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

import unittest

from src.models.Aluno import Aluno

from src.models.Pessoa import Pessoa

from src.models.Pix import Pix
from src.models.ContaBancaria import ContaBancaria


class TestaAluno(unittest.TestCase):

    def testa_heranca_pessoa(self):
        """Testa se a classe Aluno herda de Pessoa"""
        self.assertTrue(issubclass(Aluno, Pessoa))

    def testa_construtor(self):
        """Testa se o construtor da classe Aluno funciona"""
        aluno = Aluno(
            nome='João',
            data_nascimento='1999-01-01',
            cpf='12345678901',
            endereco='Rua 1',
            metodo_pagamento=Pix(
                chave='12345678901',
                tipo='cpf'
            )
        )
        # testa se a instância é da classe Aluno
        self.assertIsInstance(aluno, Aluno)
        self.assertIsInstance(aluno, Pessoa)
        # testa se os atributos foram definidos corretamente
        self.assertEqual(aluno.nome, 'João')
        self.assertEqual(aluno.data_nascimento, '1999-01-01')
        self.assertEqual(aluno.cpf, '12345678901')
        self.assertEqual(aluno.endereco, 'Rua 1')
        self.assertIsInstance(aluno.metodo_pagamento, Pix)

if __name__ == '__main__':
    unittest.main()