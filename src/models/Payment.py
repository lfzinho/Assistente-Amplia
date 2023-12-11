from datetime import date

from src.models.EventManager import EventManager
from src.models.PaymentEventListener import PaymentEventListener


# class Payment:
#     """Classe para representar um pagamento"""
#     def __init__(
#         self,
#         value: float,
#         payment_date: date,
#         reference_date: date,
#     ) -> None:
#         self.value = value
#         self.payment_date = payment_date
#         self.reference_date = reference_date


# class Payment:
#     """Classe para representar um pagamento"""
#     def __init__(
#         self,
#         value: float,
#         payment_date: date,
#         reference_date: date,
#     ) -> None:
#         self._value = value
#         self._payment_date = payment_date
#         self._reference_date = reference_date

#     @property
#     def value(self) -> float:
#         return self._value

#     @value.setter
#     def value(self, value: float) -> None:
#         self._value = value

#     @property
#     def reference_date(self) -> date:
#         return self._reference_date

#     @reference_date.setter
#     def reference_date(self, reference_date: date) -> None:
#         self._reference_date = reference_date

#     @property
#     def payment_date(self) -> date:
#         return self._payment_date

#     @payment_date.setter
#     def payment_date(self, payment_date: date) -> None:
#         self._payment_date = payment_date


# class Payment:
#     """Classe para representar um pagamento"""
#     def __init__(
#         self,
#         value: float,
#         payment_date: date,
#         reference_date: date,
#     ) -> None:
#         """
#         Construtor da classe Payment

#         Parâmetros:
#         -----------
#         value: float
#             Valor do pagamento
#         payment_date: date
#             Data do pagamento
#         reference_date: date
#             Data da aula à qual o pagamento se refere

#         Retorno:
#         --------
#         None
#         """
#         self._value = value
#         self._payment_date = payment_date
#         self._reference_date = reference_date

#     @property
#     def value(self) -> float:
#         """
#         Getter para o valor do pagamento

#         Parâmetros:
#         -----------
#         None

#         Retorno:
#         --------
#         float
#             Valor do pagamento
#         """
#         return self._value

#     @value.setter
#     def value(self, value: float) -> None:
#         """
#         Setter para o valor do pagamento

#         Parâmetros:
#         -----------
#         value: float
#             Valor do pagamento

#         Retorno:
#         --------
#         None
#         """
#         self._value = value

#     @property
#     def reference_date(self) -> date:
#         """
#         Getter para a data da aula à qual o pagamento se refere

#         Parâmetros:
#         -----------
#         None

#         Retorno:
#         --------
#         date
#             Data da aula à qual o pagamento se refere
#         """
#         return self._reference_date

#     @reference_date.setter
#     def reference_date(self, reference_date: date) -> None:
#         """
#         Setter para a data da aula à qual o pagamento se refere

#         Parâmetros:
#         -----------
#         reference_date: date
#             Data da aula à qual o pagamento se refere

#         Retorno:
#         --------
#         None
#         """
#         self._reference_date = reference_date

#     @property
#     def payment_date(self) -> date:
#         """
#         Getter para a data do pagamento

#         Parâmetros:
#         -----------
#         None

#         Retorno:
#         --------
#         date
#             Data do pagamento
#         """
#         return self._payment_date

#     @payment_date.setter
#     def payment_date(self, payment_date: date) -> None:
#         """
#         Setter para a data do pagamento

#         Parâmetros:
#         -----------
#         payment_date: date
#             Data do pagamento

#         Retorno:
#         --------
#         None
#         """
#         if payment_date < self.reference_date:
#             raise ValueError(
#                 "A data do pagamento não pode ser anterior à data da aula"
#             )
#         self._payment_date = payment_date


# class Payment:
#     """Classe para representar um pagamento"""
#     def __init__(
#         self,
#         value: float,
#         payment_date: date,
#         reference_date: date,
#     ) -> None:
#         """
#         Construtor da classe Payment

#         Parâmetros:
#         -----------
#         value: float
#             Valor do pagamento
#         payment_date: date
#             Data do pagamento
#         reference_date: date
#             Data da aula à qual o pagamento se refere

#         Retorno:
#         --------
#         None
#         """
#         self._value = value
#         self._payment_date = payment_date
#         self._reference_date = reference_date

#     @property
#     def value(self) -> float:
#         """
#         Getter para o valor do pagamento

#         Parâmetros:
#         -----------
#         None

#         Retorno:
#         --------
#         float
#             Valor do pagamento
#         """
#         return self._value

#     @value.setter
#     def value(self, value: float) -> None:
#         """
#         Setter para o valor do pagamento

#         Parâmetros:
#         -----------
#         value: float
#             Valor do pagamento

#         Retorno:
#         --------
#         None
#         """
#         if value < 0:
#             raise ValueError("O valor do pagamento não pode ser negativo")
#         self._value = value

#     @property
#     def reference_date(self) -> date:
#         """
#         Getter para a data da aula à qual o pagamento se refere

#         Parâmetros:
#         -----------
#         None

#         Retorno:
#         --------
#         date
#             Data da aula à qual o pagamento se refere
#         """
#         return self._reference_date

#     @reference_date.setter
#     def reference_date(self, reference_date: date) -> None:
#         """
#         Setter para a data da aula à qual o pagamento se refere

#         Parâmetros:
#         -----------
#         reference_date: date
#             Data da aula à qual o pagamento se refere

#         Retorno:
#         --------
#         None
#         """
#         self._reference_date = reference_date

#     @property
#     def payment_date(self) -> date:
#         """
#         Getter para a data do pagamento

#         Parâmetros:
#         -----------
#         None

#         Retorno:
#         --------
#         date
#             Data do pagamento
#         """
#         return self._payment_date

#     @payment_date.setter
#     def payment_date(self, payment_date: date) -> None:
#         """
#         Setter para a data do pagamento

#         Parâmetros:
#         -----------
#         payment_date: date
#             Data do pagamento

#         Retorno:
#         --------
#         None
#         """
#         if payment_date < self.reference_date:
#             raise ValueError(
#                 "A data do pagamento não pode ser anterior à data da aula"
#             )
#         self._payment_date = payment_date


# class Payment(EventManager):
#     """Classe para representar um pagamento"""
#     def __init__(
#         self,
#         value: float,
#         payment_date: date,
#         reference_date: date,
#     ) -> None:
#         """
#         Construtor da classe Payment.

#         Parâmetros
#         ----------
#         value: float
#             Valor do pagamento.
#         payment_date: date
#             Data do pagamento.
#         reference_date: date
#             Data da aula à qual o pagamento se refere.
#         """
#         self._value = value
#         self._payment_date = payment_date
#         self._reference_date = reference_date

#     @property
#     def value(self) -> float:
#         """
#         Getter para o valor do pagamento.

#         Retorna
#         -------
#         float
#             Valor do pagamento.
#         """
#         return self._value

#     @value.setter
#     def value(self, value: float) -> None:
#         """
#         Setter para o valor do pagamento.

#         Parâmetros
#         ----------
#         value: float
#             Valor do pagamento.
#         """
#         if value < 0:
#             raise ValueError("O valor do pagamento não pode ser negativo")
#         self._value = value

#     @property
#     def reference_date(self) -> date:
#         """
#         Getter para a data da aula à qual o pagamento se refere.

#         Retorna
#         -------
#         datetime.date
#             Data da aula à qual o pagamento se refere.
#         """
#         return self._reference_date

#     @reference_date.setter
#     def reference_date(self, reference_date: date) -> None:
#         """
#         Setter para a data da aula à qual o pagamento se refere.

#         Parâmetros
#         ----------
#         reference_date: datetime.date
#             Data da aula à qual o pagamento se refere.
#         """
#         self._reference_date = reference_date

#     @property
#     def payment_date(self) -> date:
#         """
#         Getter para a data do pagamento.

#         Retorna
#         -------
#         datetime.date
#             Data do pagamento.
#         """
#         return self._payment_date

#     @payment_date.setter
#     def payment_date(self, payment_date: date) -> None:
#         """
#         Setter para a data do pagamento.

#         Parâmetros
#         ----------
#         payment_date: datetime.date
#             Data do pagamento.
#         """
#         if payment_date < self.reference_date:
#             raise ValueError(
#                 "A data do pagamento não pode ser anterior à data da aula"
#             )
#         self._payment_date = payment_date


# class Payment(EventManager):
#     """Classe para representar um pagamento"""
#     def __init__(
#         self,
#         value: float,
#         payment_date: date,
#         reference_date: date,
#     ) -> None:
#         """
#         Construtor da classe Payment.

#         Parâmetros
#         ----------
#         value: float
#             Valor do pagamento.
#         payment_date: date
#             Data do pagamento.
#         reference_date: date
#             Data da aula à qual o pagamento se refere.
#         """
#         super().__init__()
#         self._value = value
#         self._payment_date = payment_date
#         self._reference_date = reference_date
#         # adiciona um listener para o evento de alteração do valor do pagamento
#         self.add_listener(PaymentEventListener())

#     @property
#     def value(self) -> float:
#         """
#         Getter para o valor do pagamento.

#         Retorna
#         -------
#         float
#             Valor do pagamento.
#         """
#         return self._value

#     @value.setter
#     def value(self, value: float) -> None:
#         """
#         Setter para o valor do pagamento.

#         Parâmetros
#         ----------
#         value: float
#             Valor do pagamento.
#         """
#         if value < 0:
#             raise ValueError("O valor do pagamento não pode ser negativo")
#         self._value = value

#     @property
#     def reference_date(self) -> date:
#         """
#         Getter para a data da aula à qual o pagamento se refere.

#         Retorna
#         -------
#         datetime.date
#             Data da aula à qual o pagamento se refere.
#         """
#         return self._reference_date

#     @reference_date.setter
#     def reference_date(self, reference_date: date) -> None:
#         """
#         Setter para a data da aula à qual o pagamento se refere.

#         Parâmetros
#         ----------
#         reference_date: datetime.date
#             Data da aula à qual o pagamento se refere.
#         """
#         self._reference_date = reference_date

#     @property
#     def payment_date(self) -> date:
#         """
#         Getter para a data do pagamento.

#         Retorna
#         -------
#         datetime.date
#             Data do pagamento.
#         """
#         return self._payment_date

#     @payment_date.setter
#     def payment_date(self, payment_date: date) -> None:
#         """
#         Setter para a data do pagamento.

#         Parâmetros
#         ----------
#         payment_date: datetime.date
#             Data do pagamento.
#         """
#         if payment_date < self.reference_date:
#             raise ValueError(
#                 "A data do pagamento não pode ser anterior à data da aula"
#             )
#         self._payment_date = payment_date


# class Payment(EventManager):
#     """Classe para representar um pagamento"""
#     def __init__(
#         self,
#         value: float,
#         payment_date: date,
#         reference_date: date,
#     ) -> None:
#         """
#         Construtor da classe Payment.

#         Parâmetros
#         ----------
#         value: float
#             Valor do pagamento.
#         payment_date: date
#             Data do pagamento.
#         reference_date: date
#             Data da aula à qual o pagamento se refere.
#         """
#         super().__init__()
#         self._value = value
#         self._payment_date = payment_date
#         self._reference_date = reference_date
#         # adiciona um listener para o evento de alteração do valor do pagamento
#         self.add_listener(PaymentEventListener())

#     def notify(self, event: str) -> None:
#         """Método responsável por notificar os listeners."""
#         for listener in self.listeners:
#             listener.update(event)

#     @property
#     def value(self) -> float:
#         """
#         Getter para o valor do pagamento.

#         Retorna
#         -------
#         float
#             Valor do pagamento.
#         """
#         return self._value

#     @value.setter
#     def value(self, value: float) -> None:
#         """
#         Setter para o valor do pagamento.

#         Parâmetros
#         ----------
#         value: float
#             Valor do pagamento.
#         """
#         if value < 0:
#             raise ValueError("O valor do pagamento não pode ser negativo")
#         self.notify("Valor de pagamento modificado")
#         self._value = value

#     @property
#     def reference_date(self) -> date:
#         """
#         Getter para a data da aula à qual o pagamento se refere.

#         Retorna
#         -------
#         datetime.date
#             Data da aula à qual o pagamento se refere.
#         """
#         return self._reference_date

#     @reference_date.setter
#     def reference_date(self, reference_date: date) -> None:
#         """
#         Setter para a data da aula à qual o pagamento se refere.

#         Parâmetros
#         ----------
#         reference_date: datetime.date
#             Data da aula à qual o pagamento se refere.
#         """
#         self.notify("Data de referência de pagamento modificada")
#         self._reference_date = reference_date

#     @property
#     def payment_date(self) -> date:
#         """
#         Getter para a data do pagamento.

#         Retorna
#         -------
#         datetime.date
#             Data do pagamento.
#         """
#         return self._payment_date

#     @payment_date.setter
#     def payment_date(self, payment_date: date) -> None:
#         """
#         Setter para a data do pagamento.

#         Parâmetros
#         ----------
#         payment_date: datetime.date
#             Data do pagamento.
#         """
#         if payment_date < self.reference_date:
#             raise ValueError(
#                 "A data do pagamento não pode ser anterior à data da aula"
#             )
#         self.notify("Data de pagamento modificada")
#         self._payment_date = payment_date

class Payment(EventManager):
    """Classe para representar um pagamento"""
    def __init__(
        self,
        id_payment: str,
        value: float,
        payment_date: date,
        reference_date: date,
        id_administrator: str,
        id_beneficiary: str,
        paid: bool = False,
    ) -> None:
        """
        Construtor da classe Payment.

        Parâmetros
        ----------
        value: float
            Valor do pagamento.
        payment_date: date
            Data do pagamento.
        reference_date: date
            Data da aula à qual o pagamento se refere.
        """
        super().__init__()
        self._id_payment = id_payment
        self._value = value
        self._payment_date = payment_date
        self._reference_date = reference_date
        self._id_administrator = id_administrator
        self._id_beneficiary = id_beneficiary
        self._paid = paid
        # adiciona um listener para o evento de alteração do valor do pagamento
        self.add_listener(PaymentEventListener())

    def notify(self, event: str) -> None:
        """Método responsável por notificar os listeners."""
        for listener in self.listeners:
            listener.update(event)

    @property
    def id_payment(self) -> str:
        """
        Getter para o ID do pagamento.

        Retorna
        -------
        str
            ID do pagamento.
        """
        return self._id_payment

    @id_payment.setter
    def id_payment(self, id_payment: str) -> None:
        """
        Setter para o ID do pagamento.

        Parâmetros
        ----------
        id_payment: str
            ID do pagamento.
        """
        self.notify(f"ID de pagamento modificado para pagamento {self.id_payment}")
        self._id_payment = id_payment

    @property
    def value(self) -> float:
        """
        Getter para o valor do pagamento.

        Retorna
        -------
        float
            Valor do pagamento.
        """
        return self._value

    @value.setter
    def value(self, value: float) -> None:
        """
        Setter para o valor do pagamento.

        Parâmetros
        ----------
        value: float
            Valor do pagamento.
        """
        if value < 0:
            raise ValueError("O valor do pagamento não pode ser negativo")
        self.notify(f"Valor de pagamento modificado para pagamento {self.id_payment}. Novo valor: {value}")
        self._value = value

    @property
    def reference_date(self) -> date:
        """
        Getter para a data da aula à qual o pagamento se refere.

        Retorna
        -------
        datetime.date
            Data da aula à qual o pagamento se refere.
        """
        return self._reference_date

    @reference_date.setter
    def reference_date(self, reference_date: date) -> None:
        """
        Setter para a data da aula à qual o pagamento se refere.

        Parâmetros
        ----------
        reference_date: datetime.date
            Data da aula à qual o pagamento se refere.
        """
        self.notify(f"Data de referência de pagamento modificada para pagamento {self.id_payment}. Nova data: {reference_date}")
        self._reference_date = reference_date

    @property
    def payment_date(self) -> date:
        """
        Getter para a data do pagamento.

        Retorna
        -------
        datetime.date
            Data do pagamento.
        """
        return self._payment_date

    @payment_date.setter
    def payment_date(self, payment_date: date) -> None:
        """
        Setter para a data do pagamento.

        Parâmetros
        ----------
        payment_date: datetime.date
            Data do pagamento.
        """
        if payment_date < self.reference_date:
            raise ValueError(
                "A data do pagamento não pode ser anterior à data da aula"
            )
        self.notify(f"Data de pagamento modificada para o pagamento {self.id_payment}. Nova data: {payment_date}")
        self._payment_date = payment_date

    @property
    def id_administrator(self) -> int:
        """
        Getter para o ID do administrador.

        Retorna
        -------
        int
            ID do administrador.
        """
        return self._id_administrator

    @id_administrator.setter
    def id_administrator(self, id_administrator: int) -> None:
        """
        Setter para o ID do administrador.

        Parâmetros
        ----------
        id_administrator: int
            ID do administrador.
        """
        self.notify(f"ID do administrador modificado para pagamento {self.id_payment}. Novo ID: {id_administrator}")
        self._id_administrator = id_administrator

    @property
    def id_beneficiary(self) -> str:
        """
        Getter para o ID do beneficiário.

        Retorna
        -------
        str
            ID do beneficiário.
        """
        return self._id_beneficiary

    @id_beneficiary.setter
    def id_beneficiary(self, id_beneficiary: str) -> None:
        """
        Setter para o ID do beneficiário.

        Parâmetros
        ----------
        id_beneficiary: str
            ID do beneficiário.
        """
        self.notify(f"ID do beneficiário modificado para pagamento {self.id_payment}. Novo ID: {id_beneficiary}")
        self._id_beneficiary = id_beneficiary

    @property
    def paid(self) -> bool:
        """
        Getter para o status de pagamento.

        Retorna
        -------
        bool
            Status de pagamento.
        """
        return self._paid

    @paid.setter
    def paid(self, paid: bool) -> None:
        """
        Setter para o status de pagamento.

        Parâmetros
        ----------
        paid: bool
            Status de pagamento.
        """
        self.notify(f"Status de pagamento modificado para o pagamento {self.id_payment}. Novo status: {paid}")
        self._paid = paid
