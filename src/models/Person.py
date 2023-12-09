from abc import ABC, abstractmethod
from datetime import date
from typing import Optional, Type

from src.models.PaymentMethod import PaymentMethod


# class Person:
#     """Classe que representa uma pessoa"""
#     def __init__(
#         self,
#         name: str,
#         email: str,
#         cpf: str,
#         address: str,
#         payment_method: Type[PaymentMethod],
#         birth_date: date,
#         admission_date: date,
#         exit_date: date = None,
#     ) -> None:
#         self.name = name
#         self.email = email
#         self.cpf = cpf
#         self.address = address
#         self.payment_method = payment_method
#         self.birth_date = birth_date
#         self.admission_date = admission_date
#         self.exit_date = exit_date


class Person(ABC):
    """Classe que representa uma pessoa"""
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
        exit_date: Optional[date] = None,
    ) -> None:
        """
        Construtor da classe Pessoa.

        Parâmetros
        ----------
        name : str
            Nome da pessoa.
        email : str
            Email da pessoa.
        cpf : str
            CPF da pessoa.
        address : str
            Endereço da pessoa.
        payment_method : Type[PaymentMethod]
            Método de pagamento que a pessoa irá receber reembolsos.
        birth_date : date
            Data de nascimento da pessoa.
        admission_date : date
            Data de admissão da pessoa.
        exit_date : date
            Data de saída da pessoa.
        """
        self._name = name
        self._email = email
        self._cpf = cpf
        self._address = address
        self._payment_method = payment_method
        self._birth_date = birth_date
        self._admission_date = admission_date
        self._exit_date = exit_date

    @property
    def name(self) -> str:
        """
        Getter do nome da pessoa.

        Retorna
        -------
        str
            Nome da pessoa.
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Setter do nome da pessoa.

        Parâmetros
        ----------
        name : str
            Nome da pessoa.
        """
        self._name = name

    @property
    def email(self) -> str:
        """
        Getter do email da pessoa.

        Retorna
        -------
        str
            Email da pessoa.
        """
        return self._email

    @email.setter
    def email(self, email: str) -> None:
        """
        Setter do email da pessoa.

        Parâmetros
        ----------
        email : str
            Email da pessoa.
        """
        self._email = email

    @property
    def cpf(self) -> str:
        """
        Getter do CPF da pessoa.

        Retorna
        -------
        str
            CPF da pessoa.
        """
        return self._cpf

    @cpf.setter
    def cpf(self, cpf: str) -> None:
        """
        Setter do CPF da pessoa.

        Parâmetros
        ----------
        cpf : str
            CPF da pessoa.
        """
        self._cpf = cpf

    @property
    def address(self) -> str:
        """
        Getter do endereço da pessoa.

        Retorna
        -------
        str
            Endereço da pessoa.
        """
        return self._address

    @address.setter
    def address(self, address: str) -> None:
        """
        Setter do endereço da pessoa.

        Parâmetros
        ----------
        address : str
            Endereço da pessoa.
        """
        self._address = address

    @property
    def payment_method(self) -> Type[PaymentMethod]:
        """
        Getter do método de pagamento da pessoa.

        Retorna
        -------
        Type[PaymentMethod]
            Método de pagamento da pessoa.
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method: Type[PaymentMethod]) -> None:
        """
        Setter do método de pagamento da pessoa.

        Parâmetros
        ----------
        payment_method : Type[PaymentMethod]
            Método de pagamento da pessoa.
        """
        self._payment_method = payment_method

    @property
    def birth_date(self) -> date:
        """
        Getter da data de nascimento da pessoa.

        Retorna
        -------
        date
            Data de nascimento da pessoa.
        """
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date: date) -> None:
        """
        Setter da data de nascimento da pessoa.

        Parâmetros
        ----------
        birth_date : date
            Data de nascimento da pessoa.
        """
        self._birth_date = birth_date

    @property
    def admission_date(self) -> date:
        """
        Getter da data de admissão da pessoa.

        Retorna
        -------
        date
            Data de admissão da pessoa.
        """
        return self._admission_date

    @admission_date.setter
    def admission_date(self, admission_date: date) -> None:
        """
        Setter da data de admissão da pessoa.

        Parâmetros
        ----------
        admission_date : date
            Data de admissão da pessoa.
        """
        self._admission_date = admission_date

    @property
    def exit_date(self) -> date:
        """
        Getter da data de saída da pessoa.

        Retorna
        -------
        date
            Data de saída da pessoa.
        """
        return self._exit_date

    @exit_date.setter
    def exit_date(self, exit_date: date) -> None:
        """
        Setter da data de saída da pessoa.

        Parâmetros
        ----------
        exit_date : date
            Data de saída da pessoa.
        """
        self._exit_date = exit_date
