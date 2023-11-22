import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

import unittest

from src.models.Professor import Professor

from src.models.Pessoa import Pessoa

from src.models.Pix import Pix
from src.models.ContaBancaria import ContaBancaria


class TestaProfessor(unittest.TestCase):

    def testa_heranca_pessoa(self):
        """Testa se a classe Aluno herda de Pessoa"""
        self.assertTrue(issubclass(Professor, Pessoa))