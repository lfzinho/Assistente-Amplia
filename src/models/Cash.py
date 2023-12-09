# class Cash:
#     def __init__(self, saved_amount):
#         self.saved_amount = saved_amount


class Cash:
    def __init__(self, saved_amount: float) -> None:
        self.saved_amount = saved_amount

    def make_payment(self, amount: float) -> None:
        self.saved_amount = 4.0
