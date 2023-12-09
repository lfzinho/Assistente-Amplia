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
    """Classe que armazena o saldo da instituição."""
    def __init__(self, saved_amount: float) -> None:
        """
        Construtor da classe Cash.

        Parâmetros
        ----------
        saved_amount: float
            Saldo da instituição.
        """
        self.saved_amount = saved_amount

    def make_payment(self, amount: float) -> None:
        """
        Método para fazer pagamentos.

        Parâmetros
        ----------
        amount: float
            Quantia a ser paga.

        Raises
        ------
        ValueError
            Se a quantia for negativa ou zero.
        ValueError
            Se a quantia for maior que o saldo.
        """
        if amount <= 0.0:
            raise ValueError("A quantia não pode ser negativa ou zero.")
        if amount > self.saved_amount:
            raise ValueError("A quantia não pode ser maior que o saldo.")
        self.saved_amount -= amount

