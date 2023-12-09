from datetime import date
from typing import Type

from Person import Person
from src.models.PaymentMethod import PaymentMethod


class Analyst(Person):
    """Classe que representa um analista do Amplia"""
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
        occupation_area: str =
    )
