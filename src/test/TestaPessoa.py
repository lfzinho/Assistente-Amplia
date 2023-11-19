import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import unittest
from model import Pessoa


class TestaPessoa(unittest.TestCase):

    def testa_construtor_pessoa():
        """Testa o construtor da classe Pessoa conferindo se os atributos foram setados corretamente"""
        pessoa = Pessoa(
            nome='João',
            data_nascimento='1990-01-01',
            cpf='123.456.789-00',
            endereco='Rua 1, 123'
        )
        self.assertEqual(pessoa.nome, 'João')
        self.assertEqual(pessoa.data_nascimento, '1990-01-01')
        self.assertEqual(pessoa.cpf, '123.456.789-00')
        self.assertEqual(pessoa.endereco, 'Rua 1, 123')   

 

if __name__ == '__main__':
    unittest.main()
