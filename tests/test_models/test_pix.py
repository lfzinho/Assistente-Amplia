import unittest

from . import init_path
from src.models.PaymentMethod import PaymentMethod
from src.models.Pix import Pix


class TestPix(unittest.TestCase):
    """Classe que testa a classe Pix."""
    def test_constructor(self) -> None:
        """
        Testa o construtor da classe Pix conferindo se os atributos
        foram setados corretamente.
        """
        pix = Pix('12345678910', 'cpf')
        self.assertIsInstance(pix, Pix)
        self.assertEqual(pix.key, '12345678910')
        self.assertEqual(pix.type_, 'cpf')

    def test_inheritance(self) -> None:
        """Testa se a classe Pix herda de PaymentMethod."""
        self.assertTrue(issubclass(Pix, PaymentMethod))

    def test_return_type_get_information(self) -> None:
        """
        Testa se o método get_information retorna uma string.
        """
        pix = Pix('12345678910', 'cpf')
        self.assertIsInstance(pix.get_information(), str)

    def test_return_get_information(self) -> None:
        """
        Testa se o método get_information retorna as
        informações corretas.
        """
        pix = Pix('12345678910', 'cpf')
        self.assertEqual(
            pix.get_information(),
            'Chave: 12345678910\nTipo: cpf'
        )

    def test_getters(self) -> None:
        """
        Testa se os getters funcionam corretamente.
        """
        pix = Pix('12345678910', 'cpf')
        self.assertEqual(pix.key, '12345678910')
        self.assertEqual(pix.type_, 'cpf')

    def test_setters(self) -> None:
        """Testa se os setters funcionam corretamente."""
        pix = Pix('12345678910', 'cpf')
        pix.key = '10987654321'
        pix.type_ = 'cnpj'
        self.assertEqual(pix.key, '10987654321')
        self.assertEqual(pix.type_, 'cnpj')

    def test_limitation_type(self) -> None:
        """Testa se o atributo type_ só aceita valores válidos."""
        pix = Pix('12345678910', 'cpf')
        self.assertEqual(pix.type_, 'cpf')
        pix.type_ = 'cnpj'
        self.assertEqual(pix.type_, 'cnpj')
        pix.type_ = 'email'
        self.assertEqual(pix.type_, 'email')
        pix.type_ = 'celular'
        self.assertEqual(pix.type_, 'celular')
        pix.type_ = 'aleatorio'
        self.assertEqual(pix.type_, 'aleatorio')
        # Verifica se o valor 'inválido' vai gerar uma exceção
        with self.assertRaises(ValueError):
            pix.type_ = 'invalido'
        # Verifica se o valor anterior foi mantido
        self.assertEqual(pix.type_, 'aleatorio')


if __name__ == '__main__':
    unittest.main()
