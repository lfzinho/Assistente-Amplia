from datetime import date
from typing import Literal, Optional, Type

from src.models.Person import Person
from src.models.PaymentMethod import PaymentMethod


class Analyst(Person):
    def __init__(
        self,
        name: str,
        email: str,
        cpf: str,
        address: str,
        payment_method: Type[PaymentMethod],
        birth_date: date,
        admission_date: date,
        occupation_area: Literal[occupations_areas],
        exit_date: Optional[date] = None,
    ) -> None:
        """
        Construtor da classe Analista.

        Parâmetros
        ----------
        name : str
            Nome do analista.
        email : str
            Email do analista.
        cpf : str
            CPF do analista.
        address : str
            Endereço do analista.
        payment_method : Type[PaymentMethod]
            Método de pagamento que o analista irá receber reembolsos.
        birth_date : date
            Data de nascimento do analista.
        admission_date : date
            Data de admissão do analista.
        occupation_area : str
            Área de atuação do analista.
        exit_date : Optional[date], optional
            Data de saída do analista, by default None.
        """
        super().__init__(
            name,
            email,
            cpf,
            address,
            payment_method,
            birth_date,
            admission_date,
            exit_date,
        )
        self.occupation_area = occupation_area
