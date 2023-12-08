import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

import datetime
import unittest

from src.interface.fields import TextField, DateField


class TestaTextField(unittest.TestCase):
    """Classe que testa a classe TextField"""

    def testa_informacoes_construtor(self):
        """Testa o construtor da classe TextField conferindo se os 
        atributos foram setados corretamente
        """
        text_field = TextField('Label', 'Value')
        self.assertEqual(text_field.label, 'Label')
        self.assertEqual(text_field.value, 'Value')
        self.assertEqual(text_field.type, 'text')

    def testa_tipo_retorno_get_type(self):
        """Testa se o método get_type retorna uma string"""
        text_field = TextField('Label', 'Value')
        self.assertIsInstance(text_field.get_type(), str)

    def testa_retorno_get_type(self):
        """Testa se o método get_type retorna o tipo correto"""
        text_field = TextField('Label', 'Value')
        self.assertEqual(text_field.get_type(), 'text')

    def testa_retorno_render(self):
        """Testa se o método render retorna None"""
        text_field = TextField('Label', 'Value')
        self.assertIsNone(text_field.render())

    def testa_getters(self):
        """Testa se os getters funcionam corretamente"""
        text_field = TextField('Label', 'Value')
        self.assertEqual(text_field.label, 'Label')
        self.assertEqual(text_field.value, 'Value')
        self.assertEqual(text_field.type, 'text')

    def testa_setters(self):
        """Testa se os setters funcionam corretamente"""
        text_field = TextField('Label', 'Value')
        text_field.label = 'Label2'
        text_field.value = 'Value2'
        text_field.type = 'text2'
        self.assertEqual(text_field.label, 'Label2')
        self.assertEqual(text_field.value, 'Value2')
        self.assertEqual(text_field.type, 'text2')


class TestaDateField(unittest.TestCase):
    """Classe que testa a classe DateField"""

    def testa_informacoes_construtor(self):
        """Testa o construtor da classe DateField conferindo se os 
        atributos foram setados corretamente
        """
        value = datetime.date(2002, 16, 9)
        date_field = DateField('Label', value)
        self.assertEqual(date_field.label, 'Label')
        self.assertEqual(date_field.value, value)
        self.assertEqual(date_field.type, 'date')

    def testa_tipo_retorno_get_type(self):
        """Testa se o método get_type retorna uma string"""
        value = datetime.date(2002, 16, 9)
        date_field = DateField('Label', value)
        self.assertIsInstance(date_field.get_type(), str)

    def testa_retorno_get_type(self):
        """Testa se o método get_type retorna o tipo correto"""
        value = datetime.date(2002, 16, 9)
        date_field = DateField('Label', value)
        self.assertEqual(date_field.get_type(), 'date')

    def testa_retorno_render(self):
        """Testa se o método render retorna None"""
        date_field = DateField('Label', 'Value')
        self.assertIsNone(date_field.render())

    def testa_getters(self):
        """Testa se os getters funcionam corretamente"""
        value = datetime.date(2002, 16, 9)
        date_field = DateField('Label', value)
        self.assertEqual(date_field.label, 'Label')
        self.assertEqual(date_field.value, value)
        self.assertEqual(date_field.type, 'date')

    def testa_setters(self):
        """Testa se os setters funcionam corretamente"""
        value1 = datetime.date(2002, 16, 9)
        value2 = datetime.date(2003, 2, 4)
        date_field = DateField('Label', value1)
        date_field.label = 'Label2'
        date_field.value = value2
        date_field.type = 'date2'
        self.assertEqual(date_field.label, 'Label2')
        self.assertEqual(date_field.value, value2)
        self.assertEqual(date_field.type, 'date2')


if __name__ == '__main__':
    unittest.main()
    