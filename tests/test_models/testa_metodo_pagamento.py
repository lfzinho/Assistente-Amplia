import unittest

from . import init_path
from src.models.MetodoPagamento import MetodoPagamento


class TestaMetodoPagamento(unittest.TestCase):
    def test_init_is_abstract(self) -> None:
        self.assertIn('__init__', MetodoPagamento.__abstractmethods__)

    def test_visualizar_informacoes_is_abstract(self) -> None:
        self.assertIn(
            'visualizar_informacoes',
            MetodoPagamento.__abstractmethods__
        )

    def test_eh_abstract(self) -> None:
        self.assertTrue(MetodoPagamento.__abstractmethods__)


if __name__ == '__main__':
    unittest.main()
