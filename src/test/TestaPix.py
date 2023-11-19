import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import unittest
from model.MetodoPagamento import MetodoPagamento
from model.Pix import Pix

class TestaPix(unittest.TestCase):

    def testa_informacoes_construtor(self):
        """Testa o construtor da classe Pix conferindo se os atributos foram setados corretamente"""
        pix = Pix('12345678910', 'cpf')
        self.assertEqual(pix.chave, '12345678910')
        self.assertEqual(pix.tipo, 'cpf')

    def testa_heranca_metodo_pagamento(self):
        """Testa se a classe Pix herda de MetodoPagamento"""
        self.assertTrue(issubclass(Pix, MetodoPagamento))

    def testa_retorno_metodo_pagamento(self):
        """Testa se o método visualizar_informacoes retorna uma string"""
        pix = Pix('12345678910', 'cpf')
        self.assertIsInstance(pix.visualizar_informacoes(), str)

if __name__ == '__main__':
    unittest.main()
