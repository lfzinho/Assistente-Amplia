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


if __name__ == '__main__':
    unittest.main()