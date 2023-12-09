import unittest

from . import init_path
from src.models.Pix import Pix
from src.models.Teacher import Teacher


class TestTeacher(unittest.TestCase):
    def test_constructor(self) -> None:
        """
        Testa o construtor da classe Teacher conferindo se os
        atributos foram setados corretamente.
        """
        teacher = Teacher(
            name='João',
            email='joaosilva@gmail.com',
            cpf='123.456.789-00',
            address='Rua 1, 123',
            payment_method=Pix(key='12345678900', type_='cpf'),
            birth_date='1990-01-01',
            admission_date='2021-01-01',
            exit_date='2021-02-01',
            transport_cost=10.0,
            transport_description='Uber',
            theme='Math',
        )
        self.assertIsInstance(teacher, Teacher)
        self.assertEqual(teacher.theme, 'Math')

    def test_inheritance(self) -> None:
        """Testa se Teacher herda de Beneficiary."""
        from src.models.Beneficiary import Beneficiary
        self.assertTrue(issubclass(Teacher, Beneficiary))

    def test_getters(self) -> None:
        """Testa se os getters de Teacher funcionam corretamente."""
        teacher = Teacher(
            name='João',
            email='joaosilva@gmail.com',
            cpf='123.456.789-00',
            address='Rua 1, 123',
            payment_method=Pix(key='12345678900', type_='cpf'),
            birth_date='1990-01-01',
            admission_date='2021-01-01',
            exit_date='2021-02-01',
            transport_cost=10.0,
            transport_description='Uber',
            theme='Math',
        )
        self.assertEqual(teacher.theme, 'Math')

    def test_setters(self) -> None:
        """Testa se os setters de Teacher funcionam corretamente."""
        teacher = Teacher(
            name='João',
            email='joaosilva@gmail.com',
            cpf='123.456.789-00',
            address='Rua 1, 123',
            payment_method=Pix(key='12345678900', type_='cpf'),
            birth_date='1990-01-01',
            admission_date='2021-01-01',
            exit_date='2021-02-01',
            transport_cost=10.0,
            transport_description='Uber',
            theme='Math',
        )
        teacher.theme = 'Portuguese'
        self.assertEqual(teacher.theme, 'Portuguese')


if __name__ == '__main__':
    unittest.main()
