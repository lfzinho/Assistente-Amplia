from src.models.PaymentMethod import PaymentMethod


# class BankAccount:
#     def __init__(self, bank: str, agency: int, account_number: int) -> None:
#         self._bank = bank
#         self._agency = agency
#         self._account_number = account_number


# class BankAccount(PaymentMethod):
#     def __init__(self, bank: str, agency: int, account_number: int) -> None:
#         self._bank = bank
#         self._agency = agency
#         self._account_number = account_number

#     def view_information(self) -> str:
#         pass


# class BankAccount(PaymentMethod):
#     def __init__(self, bank: str, agency: int, account_number: int) -> None:
#         self._bank = bank
#         self._agency = agency
#         self._account_number = account_number

#     def view_information(self) -> str:
#         return (
#             f'Banco: {self._bank}\nAgência: {self._agency}\n'
#             f'Número da conta: {self._account_number}'
#         )


class BankAccount(PaymentMethod):
    """Classe que representa um método de pagamento Conta Bancária."""
    def __init__(self, bank: str, agency: int, account_number: int) -> None:
        """
        Construtor da classe ContaBancaria.

        Parâmetros
        ----------
        bank : str
            Nome do banco.
        agency : int
            Número da agência.
        account_number : int
            Número da conta.
        """
        self._bank = bank
        self._agency = agency
        self._account_number = account_number
        self.class_ = 'BankAccount'

    def get_information(self) -> str:
        """
        Retorna uma string com as informações da Conta Bancária.

        Retorna
        -------
        str
            Informações da Conta Bancária.
        """
        return (
            f'Banco: {self._bank}\nAgência: {self._agency}\n'
            f'Número da conta: {self._account_number}'
        )

    @property
    def bank(self) -> str:
        """
        Getter do nome do banco.

        Retorna
        -------
        str
            Nome do banco.
        """
        return self._bank

    @bank.setter
    def bank(self, bank: str) -> None:
        """
        Setter do nome do banco.

        Parâmetros
        ----------
        bank : str
            Nome do banco.

        Retorna
        -------
        None
        """
        self._bank = bank

    @property
    def agency(self) -> int:
        """
        Getter do número da agência.

        Retorna
        -------
        int
            Número da agência.
        """
        return self._agency

    @agency.setter
    def agency(self, agency: int) -> None:
        """
        Setter do número da agência.

        Parâmetros
        ----------
        agency : int
            Número da agência.

        Retorna
        -------
        None
        """
        self._agency = agency

    @property
    def account_number(self) -> int:
        """
        Getter do número da conta.

        Retorna
        -------
        int
            Número da conta.
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number: int) -> None:
        """
        Setter do número da conta.

        Parâmetros
        ----------
        account_number : int
            Número da conta.

        Retorna
        -------
        None
        """
        self._account_number = account_number

