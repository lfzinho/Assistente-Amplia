import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import unittest
from model.Pix import Pix

class TestaPix(unittest.TestCase):
    """Testa o construtor da classe Pix conferindo se os atributos foram setados corretamente"""
    pix = Pix('12345678910', 'cpf')
    self.assertEqual(pix.chave, '12345678910')
    self.assertEqual(pix.tipo, 'cpf')

if __name__ == '__main__':
    unittest.main()
