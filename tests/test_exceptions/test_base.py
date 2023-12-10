import unittest

from src.exceptions.base import BaseError


class TestBaseError(unittest.TestCase):
    def create_derived_error(self, msg: str | None = None) -> BaseError:
        """Cria uma exceção derivada de BaseError para testes."""
        if msg:
            class Error(BaseError):
                def message(self) -> str:
                    return msg
        else:
            class Error(BaseError):
                pass
        return Error

    def test_abstract_message(self) -> None:
        """
        Verifica se a classe não é instanciada quando o atributo
        abstrato não é definido.
        """
        Error = self.create_derived_error()
        self.assertRaises(TypeError, Error)

    def test_message(self) -> None:
        """
        Verifica se a exceção contém a mensagem
        padrão quando nenhuma é passada no construtor.
        """
        message = 'Mensagem Padrão'
        Error = self.create_derived_error(message)
        error = Error()
        self.assertEqual(error.args[0], message)

    def test_custom_message(self) -> None:
        """Verifica se a exceção contém a mensagem passada."""
        message = 'Mensagem Personalizada'
        Error = self.create_derived_error('Mensagem padrão')
        error = Error(message)
        self.assertEqual(error.args[0], message)

    def test_raise(self) -> None:
        """Verifica se a exceção é levantada corretamente."""
        message = 'Mensagem de erro'
        Error = self.create_derived_error(message)

        def raise_error() -> None:
            raise Error()
        self.assertRaises(Error, raise_error)
