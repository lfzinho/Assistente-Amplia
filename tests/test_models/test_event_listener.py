import unittest

from src.models.EventListener import EventListener


class TestEventListener(unittest.TestCase):
    """Classe responsável por testar a classe EventListener."""
    def test_is_abstract(self) -> None:
        """
        Testa se a classe EventListener é abstrata conferindo se
        ela não pode ser instanciada.
        """
        with self.assertRaises(TypeError):
            EventListener()

    def test_has_update_method(self):
        """
        Testa se a classe EventListener possui o método update
        conferindo se ele está presente na classe.
        """
        self.assertTrue(hasattr(EventListener, 'update'))


if __name__ == '__main__':
    unittest.main()
