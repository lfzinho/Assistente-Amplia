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
        self.value = value
        self.payment_date = payment_date
        self.reference_date = reference_date
