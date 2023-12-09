from datetime import date
from typing import Optional, Type

from src.models.PaymentMethod import PaymentMethod
from src.models.Beneficiary import Beneficiary


class Student(Beneficiary):
    """Classe que representa um aluno."""
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
        financial_manager: str,
        exit_date: Optional[date] = None,
    ) -> None:
        super().__init__(
            name=name,
            email=email,
            cpf=cpf,
            address=address,
            payment_method=payment_method,
            birth_date=birth_date,
            admission_date=admission_date,
            transport_cost=transport_cost,
            transport_description=transport_description,
            exit_date=exit_date
        )
        self.financial_manager = financial_manager
