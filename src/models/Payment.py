from datetime import date


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


class Payment:
    """Classe para representar um pagamento"""
    def __init__(
        self,
        value: float,
        payment_date: date,
        reference_date: date,
    ) -> None:
        """
        Construtor da classe Payment

        Parâmetros:
        -----------
        value: float
            Valor do pagamento
        payment_date: date
            Data do pagamento
        reference_date: date
            Data da aula à qual o pagamento se refere

        Retorno:
        --------
        None
        """
        self._value = value
        self._payment_date = payment_date
        self._reference_date = reference_date
        self.class_ = 'Payment'

    @property
    def value(self) -> float:
        """
        Getter para o valor do pagamento

        Parâmetros:
        -----------
        None

        Retorno:
        --------
        float
            Valor do pagamento
        """
        return self._value

    @value.setter
    def value(self, value: float) -> None:
        """
        Setter para o valor do pagamento

        Parâmetros:
        -----------
        value: float
            Valor do pagamento

        Retorno:
        --------
        None
        """
        if value < 0:
            raise ValueError("O valor do pagamento não pode ser negativo")
        self._value = value

    @property
    def reference_date(self) -> date:
        """
        Getter para a data da aula à qual o pagamento se refere

        Parâmetros:
        -----------
        None

        Retorno:
        --------
        date
            Data da aula à qual o pagamento se refere
        """
        return self._reference_date

    @reference_date.setter
    def reference_date(self, reference_date: date) -> None:
        """
        Setter para a data da aula à qual o pagamento se refere

        Parâmetros:
        -----------
        reference_date: date
            Data da aula à qual o pagamento se refere

        Retorno:
        --------
        None
        """
        self._reference_date = reference_date

    @property
    def payment_date(self) -> date:
        """
        Getter para a data do pagamento

        Parâmetros:
        -----------
        None

        Retorno:
        --------
        date
            Data do pagamento
        """
        return self._payment_date

    @payment_date.setter
    def payment_date(self, payment_date: date) -> None:
        """
        Setter para a data do pagamento

        Parâmetros:
        -----------
        payment_date: date
            Data do pagamento

        Retorno:
        --------
        None
        """
        if payment_date < self.reference_date:
            raise ValueError(
                "A data do pagamento não pode ser anterior à data da aula"
            )
        self._payment_date = payment_date
