from datetime import date
from typing import Optional, Type

from src.models.Beneficiary import Beneficiary
from src.models.PaymentMethod import PaymentMethod


class Teacher(Beneficiary):
    """
    Classe que representa um professor.

    Parâmetros
    ----------
    name : str
        Nome do professor.
    email : str
        Email do professor.
    cpf : str
        CPF do professor.
    address : str
        Endereço do professor.
    payment_method : Type[PaymentMethod]
        Método de pagamento do professor.
    birth_date : date
        Data de nascimento do professor.
    admission_date : date
        Data de admissão do professor.
    transport_cost : float
        Custo do transporte do professor.
    transport_description : str
        Descrição do transporte do professor.
    theme : str
        Tema do professor.
    exit_date : Optional[date], optional
        Data de saída do professor.
    """
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
        theme: str,
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
        self.theme = theme

    @property
    def theme(self) -> str:
        """Getter do tema."""
        return self._theme

    @theme.setter
    def theme(self, theme: str) -> None:
        """Setter do tema."""
        self._theme = theme
