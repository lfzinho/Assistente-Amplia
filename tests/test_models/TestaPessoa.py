import unittest
from src.models import Pessoa


class TestaPessoa(unittest.TestCase):

    def testa_construtor_pessoa(self):
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
