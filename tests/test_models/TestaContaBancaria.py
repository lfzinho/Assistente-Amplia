import unittest
from src.models.MetodoPagamento import MetodoPagamento
from src.models.ContaBancaria import ContaBancaria

class TestaContaBancaria(unittest.TestCase):
    """Classe que testa a classe ContaBancaria"""

    def testa_informacoes_construtor(self):
        """Testa o construtor da classe ContaBancaria conferindo se os atributos foram setados corretamente"""
        conta_bancaria = ContaBancaria('Itaú', '123456', '12345678')
        self.assertEqual(conta_bancaria._agencia, '123456')
        self.assertEqual(conta_bancaria._nro_conta, '12345678')
        self.assertEqual(conta_bancaria._banco, 'Itaú')

    def testa_heranca_metodo_pagamento(self):
        """Testa se a classe ContaBancaria herda de MetodoPagamento"""
        self.assertTrue(issubclass(ContaBancaria, MetodoPagamento))

    def testa_tipo_retorno_visualizar_informacoes(self):
        """Testa se o método visualizar_informacoes retorna uma string"""
        conta_bancaria = ContaBancaria('Itaú', '123456', '12345678')
        self.assertIsInstance(conta_bancaria.visualizar_informacoes(), str)
    
    def testa_retorno_vizualizar_informacoes(self):
        """Testa se o método visualizar_informacoes retorna as informações corretas"""
        conta_bancaria = ContaBancaria('Itaú', '123456', '12345678')
        self.assertEqual(conta_bancaria.visualizar_informacoes(), "Banco: Itaú\nAgência: 123456\nNúmero da conta: 12345678")

    def testa_getters(self):
        """Testa se os getters funcionam corretamente"""
        conta_bancaria = ContaBancaria('Itaú', '123456', '12345678')
        self.assertEqual(conta_bancaria.banco, 'Itaú')
        self.assertEqual(conta_bancaria.agencia, '123456')
        self.assertEqual(conta_bancaria.nro_conta, '12345678')

    def testa_setters(self):
        """Testa se os setters funcionam corretamente"""
        conta_bancaria = ContaBancaria('Itaú', '123456', '12345678')
        conta_bancaria.banco = 'Bradesco'
        conta_bancaria.agencia = '654321'
        conta_bancaria.nro_conta = '87654321'
        self.assertEqual(conta_bancaria.banco, 'Bradesco')
        self.assertEqual(conta_bancaria.agencia, '654321')
        self.assertEqual(conta_bancaria.nro_conta, '87654321')
        

if __name__ == '__main__':
    unittest.main()
        