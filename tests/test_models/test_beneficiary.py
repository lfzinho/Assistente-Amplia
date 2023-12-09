import unittest
from abc import ABC

from . import init_path
from src.models.Beneficiary import Beneficiary


class TestBeneficiary(unittest.TestCase):
    def test_constructor(self) -> None:
        """
        Testa o construtor da classe Beneficiary conferindo se os
        atributos foram setados corretamente.
        """
        beneficiary = Beneficiary(
            transport_cost=10.0,
            transport_description='Uber'
        )
        self.assertIsInstance(beneficiary, Beneficiary)
        self.assertEqual(beneficiary.transport_cost, 10.0)
        self.assertEqual(beneficiary.transport_description, 'Uber')
