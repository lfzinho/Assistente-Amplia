from abc import ABC, abstractmethod
from datetime import date
from typing import Type

from src.models.PaymentMethod import PaymentMethod


class Person:
    """Classe que representa uma pessoa"""
    def __init__(
        self,
        name: str,
        email: str,
        cpf: str,
        address: str,
        payment_method: Type[PaymentMethod],
        birth_date: date,
        admission_date: date,
        exit_date: date = None,
    ) -> None:
        self.name = name
        self.email = email
        self.cpf = cpf
        self.address = address
        self.payment_method = payment_method
        self.birth_date = birth_date
        self.admission_date = admission_date
        self.exit_date = exit_date

