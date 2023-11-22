import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

import unittest
from src.models.Pessoa import Pessoa
from src.models.Pix import Pix


class TestaPessoa(unittest.TestCase):

    def testa_construtor_pessoa(self):
        """Testa o construtor da classe Pessoa conferindo se os atributos foram setados corretamente"""
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

    def testa_getters(self):
        """Testa os getters da classe Pessoa"""
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
        self.assertEqual(pessoa._metodo_pagamento.visualizar_informacoes(), 'Chave: 12345678900\nTipo: cpf')

if __name__ == '__main__':
    unittest.main()
