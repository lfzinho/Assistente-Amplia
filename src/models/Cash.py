# class Cash:
#     def __init__(self, saved_amount):
#         self.saved_amount = saved_amount


# class Cash:
#     def __init__(self, saved_amount: float) -> None:
#         self.saved_amount = saved_amount

#     def make_payment(self, amount: float) -> None:
#         self.saved_amount = 4.0


# class Cash:
#     def __init__(self, saved_amount: float) -> None:
#         self.saved_amount = saved_amount

#     def make_payment(self, amount: float) -> None:
#         if amount <= 0.0:
#             raise ValueError("A quantia não pode ser negativa ou zero.")
#         self.saved_amount -= amount


class Cash:
    def __init__(self, saved_amount: float) -> None:
        self.saved_amount = saved_amount

    def make_payment(self, amount: float) -> None:
        if amount <= 0.0:
            raise ValueError("A quantia não pode ser negativa ou zero.")
        if amount > self.saved_amount:
            raise ValueError("A quantia não pode ser maior que o saldo.")
        self.saved_amount -= amount

