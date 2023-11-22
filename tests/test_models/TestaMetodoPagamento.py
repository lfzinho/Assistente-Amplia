import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

import unittest

from src.models import MetodoPagamento


class TestaMetodoPagamento(unittest.TestCase):
    def test_init_is_abstract(self):
        self.assertIn('__init__', MetodoPagamento.__abstractmethods__)

    def test_visualizar_informacoes_is_abstract(self):
        self.assertIn('visualizar_informacoes', MetodoPagamento.__abstractmethods__)
        
    def test_eh_abstract(self):
        self.assertTrue(MetodoPagamento.__abstractmethods__)


if __name__ == '__main__':
    unittest.main()
