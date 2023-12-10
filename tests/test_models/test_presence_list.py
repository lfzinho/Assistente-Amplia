import unittest
from abc import ABC
from datetime import date

from src.models.BankAccount import BankAccount
from src.models.PaymentMethod import PaymentMethod
from src.models.Pix import Pix
from src.models.PresenceList import PresenceList

class TestPresenceList(unittest.TestCase):

    def test_constructor(self) -> None:
        """
        Testa o construtor da classe PresenceList conferindo se os
        atributos foram definidos corretamente.
        """
        presence_list = PresenceList(
            class_date=date(2021, 9, 1),
            presence_ids=[1, 2, 4, 10],
        )
        self.assertIsInstance(presence_list, PresenceList)
        self.assertEqual(presence_list.class_date, date(2021, 9, 1))
        self.assertEqual(presence_list.presence_ids, [1, 2, 4, 10])

    def test_invalid_date(self) -> None:
        """
        Testa o construtor da classe PresenceList conferindo se é
        levantado erro ao passar data inválida.
        """
        with self.assertRaises(ValueError):
            PresenceList(
                class_date='invalid_value',
                presence_ids=[1, 2, 3],
            )

    def test_uniqueness(self) -> None:
        """
        Testa o construtor da classe PresenceList conferindo se é
        levantado erro ao passar ids repetidos.
        """
        with self.assertRaises(ValueError):
            PresenceList(
                class_date=date(2021, 9, 1),
                presence_ids=[1, 2, 3, 3],
            )

    def test_date_fromiso(self) -> None:
        """
        Testa o construtor da classe PresenceList conferindo se a data
        pode ser passada como string.
        """
        presence_list = PresenceList(
            class_date='2021-09-01',
            presence_ids=[1, 2, 3],
        )
        self.assertEqual(presence_list.class_date, date(2021, 9, 1))


