from abc import ABC, abstractmethod
from datetime import date
from typing import Optional, Type

from src.models.PaymentMethod import PaymentMethod
from src.models.Person import Person


# class Beneficiary:
#     """Classe que representa um beneficiário."""
#     def __init__(self, transport_cost: float, transport_description: str) -> None:
#         self.transport_cost = transport_cost
#         self.transport_description = transport_description


class Beneficiary(Person, ABC):
    """Classe que representa um beneficiário."""
    @abstractmethod
    def __init__(
        self,
        name: str,
        email: str,
        cpf: str,
        address: str,
        payment_method: Type[PaymentMethod],
        birth_date: date,
        admission_date: date,
        transport_cost: float,
        transport_description: str,
        exit_date: Optional[date] = None
    ) -> None:
        super().__init__(
            name=name,
            email=email,
            cpf=cpf,
            address=address,
            payment_method=payment_method,
            birth_date=birth_date,
            admission_date=admission_date,
            exit_date=exit_date
        )
        self.transport_cost = transport_cost
        self.transport_description = transport_description
        self.class_ = 'Beneficiary'
