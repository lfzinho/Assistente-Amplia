from datetime import date
from typing import Optional, Type

from src.models.Beneficiary import Beneficiary
from src.models.PaymentMethod import PaymentMethod


# class Student(Beneficiary):
#     """Classe que representa um aluno."""
#     def __init__(
#         self,
#         name: str,
#         email: str,
#         cpf: str,
#         address: str,
#         payment_method: Type[PaymentMethod],
#         birth_date: date,
#         admission_date: date,
#         transport_cost: float,
#         transport_description: str,
#         financial_manager: str,
#         exit_date: Optional[date] = None,
#     ) -> None:
#         super().__init__(
#             name=name,
#             email=email,
#             cpf=cpf,
#             address=address,
#             payment_method=payment_method,
#             birth_date=birth_date,
#             admission_date=admission_date,
#             transport_cost=transport_cost,
#             transport_description=transport_description,
#             exit_date=exit_date
#         )
#         self.financial_manager = financial_manager


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
        """Construtor da classe Student.

        Args:
            name (str): Nome do aluno.
            email (str): Email do aluno.
            cpf (str): CPF do aluno.
            address (str): Endereço do aluno.
            payment_method (Type[PaymentMethod]): Método de pagamento do aluno.
            birth_date (date): Data de nascimento do aluno.
            admission_date (date): Data de admissão do aluno.
            transport_cost (float): Custo do transporte do aluno.
            transport_description (str): Descrição do transporte do aluno.
            financial_manager (str): Responsável financeiro do aluno.
            exit_date (Optional[date], optional): Data de saída do aluno. Defaults to None.
        """
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

    @property
    def financial_manager(self) -> str:
        """Getter para o atributo financial_manager."""
        return self._financial_manager

    @financial_manager.setter
    def financial_manager(self, financial_manager: str) -> None:
        """Setter para o atributo financial_manager."""
        self._financial_manager = financial_manager
