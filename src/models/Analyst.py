from datetime import date
from typing import Literal, Optional, Type

from src.models.Person import Person
from src.models.PaymentMethod import PaymentMethod


# class Analyst(Person):
#     def __init__(
#         self,
#         name: str,
#         email: str,
#         cpf: str,
#         address: str,
#         payment_method: Type[PaymentMethod],
#         birth_date: date,
#         admission_date: date,
#         occupation_area: Literal[occupations_areas],
#         exit_date: Optional[date] = None,
#     ) -> None:
#         """
#         Construtor da classe Analista.

#         Parâmetros
#         ----------
#         name : str
#             Nome do analista.
#         email : str
#             Email do analista.
#         cpf : str
#             CPF do analista.
#         address : str
#             Endereço do analista.
#         payment_method : Type[PaymentMethod]
#             Método de pagamento que o analista irá receber reembolsos.
#         birth_date : date
#             Data de nascimento do analista.
#         admission_date : date
#             Data de admissão do analista.
#         occupation_area : str
#             Área de atuação do analista.
#         exit_date : Optional[date], optional
#             Data de saída do analista, by default None.
#         """
#         super().__init__(
#             name,
#             email,
#             cpf,
#             address,
#             payment_method,
#             birth_date,
#             admission_date,
#             exit_date,
#         )
#         self.occupation_area = occupation_area


class Analyst(Person):
    """Classe que representa um analista do Amplia"""

    occupations_areas: list[str] = [
        'Administrativo Financeiro',
        'Recursos Humanos',
        'Pedagógico',
        'Marketing',
    ]

    def __init__(
        self,
        name: str,
        email: str,
        cpf: str,
        address: str,
        payment_method: Type[PaymentMethod],
        birth_date: date,
        admission_date: date,
        occupation_area: Literal[
            'Administrativo Financeiro',
            'Recursos Humanos',
            'Pedagógico',
            'Marketing'
        ],
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

    @property
    def occupation_area(self) -> str:
        """Getter da área de atuação do analista."""
        return self._occupation_area

    @occupation_area.setter
    def occupation_area(self, occupation_area: str) -> None:
        """Setter da área de atuação do analista."""
        if occupation_area not in self.occupations_areas:
            raise ValueError(
                f"'{occupation_area}' não é uma área de atuação válida. "
                f"Áreas de atuação válidas: {self.occupations_areas}"
            )
        self._occupation_area = occupation_area
