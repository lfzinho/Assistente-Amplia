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


class Payment:
    """Classe para representar um pagamento"""
    def __init__(
        self,
        value: float,
        payment_date: date,
        reference_date: date,
    ) -> None:
        self._value = value
        self._payment_date = payment_date
        self._reference_date = reference_date

    @property
    def value(self) -> float:
        return self._value

    @property
    def payment_date(self) -> date:
        return self._payment_date

    @property
    def reference_date(self) -> date:
        return self._reference_date

