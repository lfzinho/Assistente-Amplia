import unittest

from . import init_path
from src.models.Pix import Pix
from src.models.Student import Student


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
            financial_manager='Maria',
        )
        self.assertIsInstance(student, Student)
        self.assertEqual(student.transport_cost, 10.0)
        self.assertEqual(student.transport_description, 'Uber')
        self.assertEqual(student.financial_manager, 'Maria')

    def test_inheritance(self) -> None:
        """Testa se Student herda de Beneficiary."""
        from src.models.Beneficiary import Beneficiary
        self.assertTrue(issubclass(Student, Beneficiary))

    def test_getters(self) -> None:
        """Testa se os getters de Student funcionam corretamente."""
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
            financial_manager='Maria',
        )
        self.assertEqual(student.name, 'João')
        self.assertEqual(student.email, 'joaosilva@gmail.com')
        self.assertEqual(student.cpf, '123.456.789-00')
        self.assertEqual(student.address, 'Rua 1, 123')
        self.assertIsInstance(student.payment_method, Pix)
        self.assertEqual(student.birth_date, '1990-01-01')
        self.assertEqual(student.admission_date, '2021-01-01')
        self.assertEqual(student.exit_date, '2021-02-01')
        self.assertEqual(student.transport_cost, 10.0)
        self.assertEqual(student.transport_description, 'Uber')
        self.assertEqual(student.financial_manager, 'Maria')

    def test_setters(self) -> None:
        """Testa se os setters de Student funcionam corretamente."""
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
            financial_manager='Maria',
        )
        student.name = 'Maria'
        student.email = 'mariasouza@hotmail.com'
        student.cpf = '987.654.321-00'
        student.address = 'Rua 2, 456'
        student.payment_method = Pix(key='98765432100', type_='cpf')
        student.birth_date = '1991-01-01'
        student.admission_date = '2021-02-01'
        student.exit_date = '2021-03-01'
        student.transport_cost = 20.0
        student.transport_description = 'Cabify'
        student.financial_manager = 'João'
        self.assertEqual(student.name, 'Maria')
        self.assertEqual(student.email, 'mariasouza@hotmail.com')
        self.assertEqual(student.cpf, '987.654.321-00')
        self.assertEqual(student.address, 'Rua 2, 456')
        self.assertIsInstance(student.payment_method, Pix)
        self.assertEqual(student.birth_date, '1991-01-01')
        self.assertEqual(student.admission_date, '2021-02-01')
        self.assertEqual(student.exit_date, '2021-03-01')
        self.assertEqual(student.transport_cost, 20.0)
        self.assertEqual(student.transport_description, 'Cabify')
        self.assertEqual(student.financial_manager, 'João')


if __name__ == '__main__':
    unittest.main()
