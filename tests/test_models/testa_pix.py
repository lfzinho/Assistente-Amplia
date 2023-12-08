import unittest

from . import init_path
from src.models.MetodoPagamento import MetodoPagamento
from src.models.Pix import Pix


class TestaPix(unittest.TestCase):
    """Classe que testa a classe Pix."""
    def testa_construtor(self):
        """
        Testa o construtor da classe Pix conferindo se os atributos
        foram setados corretamente.
        """
        pix = Pix('12345678910', 'cpf')
        self.assertIsInstance(pix, Pix)
        self.assertEqual(pix.chave, '12345678910')
        self.assertEqual(pix.tipo, 'cpf')

    def testa_heranca_metodo_pagamento(self):
        """Testa se a classe Pix herda de MetodoPagamento."""
        self.assertTrue(issubclass(Pix, MetodoPagamento))

    def testa_tipo_retorno_visualizar_informacoes(self):
        """
        Testa se o método visualizar_informacoes retorna uma string.
        """
        pix = Pix('12345678910', 'cpf')
        self.assertIsInstance(pix.visualizar_informacoes(), str)

    def testa_retorno_vizualizar_informacoes(self):
        """
        Testa se o método visualizar_informacoes retorna as
        informações corretas.
        """
        pix = Pix('12345678910', 'cpf')
        self.assertEqual(
            pix.visualizar_informacoes(),
            'Chave: 12345678910\nTipo: cpf'
        )

    def testa_getters(self):
        """
        Testa se os getters funcionam corretamente.
        """
        pix = Pix('12345678910', 'cpf')
        self.assertEqual(pix.chave, '12345678910')
        self.assertEqual(pix.tipo, 'cpf')

    def testa_setters(self):
        """Testa se os setters funcionam corretamente."""
        pix = Pix('12345678910', 'cpf')
        pix.chave = '10987654321'
        pix.tipo = 'cnpj'
        self.assertEqual(pix.chave, '10987654321')
        self.assertEqual(pix.tipo, 'cnpj')

    def testa_limitacao_tipo(self):
        """Testa se o atributo tipo só aceita valores válidos."""
        pix = Pix('12345678910', 'cpf')
        self.assertEqual(pix.tipo, 'cpf')
        pix.tipo = 'cnpj'
        self.assertEqual(pix.tipo, 'cnpj')
        pix.tipo = 'email'
        self.assertEqual(pix.tipo, 'email')
        pix.tipo = 'celular'
        self.assertEqual(pix.tipo, 'celular')
        # Verifica se o valor 'inválido' vai gerar uma exceção
        with self.assertRaises(ValueError):
            pix.tipo = 'invalido'
        # Verifica se o valor anterior foi mantido
        self.assertEqual(pix.tipo, 'celular')


if __name__ == '__main__':
    unittest.main()
