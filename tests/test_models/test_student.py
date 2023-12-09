import unittest

from . import init_path
from src.models.Student import Student
from src.models.Pix import Pix


class TestStudent(unittest.TestCase):
    def test_constructor(self) -> None:
        """
        Testa o construtor da classe Student conferindo se os
        atributos foram setados corretamente.
        """
        student = Student(
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
            financial_manager='Maria'
        )
        self.assertIsInstance(student, Student)
        self.assertEqual(student.transport_cost, 10.0)
        self.assertEqual(student.transport_description, 'Uber')
        self.assertEqual(student.financial_manager, 'Maria')


if __name__ == '__main__':
    unittest.main()
