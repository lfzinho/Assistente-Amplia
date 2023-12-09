from src.models.MetodoPagamento import MetodoPagamento


# class ContaBancaria:

#     def __init__(self, banco:str, agencia:int, nro_conta:int) -> None:
#         self._banco = banco
#         self._agencia = agencia
#         self._nro_conta = nro_conta

# class ContaBancaria(MetodoPagamento):

#     def __init__(self, banco:str, agencia:int, nro_conta:int) -> None:
#         self._banco = banco
#         self._agencia = agencia
#         self._nro_conta = nro_conta

#     def visualizar_informacoes(self):
#         pass

# class ContaBancaria(MetodoPagamento):

#     def __init__(self, banco:str, agencia:int, nro_conta:int) -> None:
#         self._banco = banco
#         self._agencia = agencia
#         self._nro_conta = nro_conta

#     def visualizar_informacoes(self):
#         return f'Banco: {self._banco}\nAgência: {self._agencia}\nNúmero da conta: {self._nro_conta}'


class ContaBancaria(MetodoPagamento):
    def __init__(self, banco: str, agencia: int, nro_conta: int) -> None:
        self._banco = banco
        self._agencia = agencia
        self._nro_conta = nro_conta

    def visualizar_informacoes(self) -> str:
        return (
            f'Banco: {self._banco}\nAgência: {self._agencia}\n'
            f'Número da conta: {self._nro_conta}'
        )

    @property
    def banco(self) -> str:
        return self._banco

    @banco.setter
    def banco(self, banco: str) -> None:
        self._banco = banco

    @property
    def agencia(self) -> int:
        return self._agencia

    @agencia.setter
    def agencia(self, agencia: int) -> None:
        self._agencia = agencia

    @property
    def nro_conta(self) -> int:
        return self._nro_conta

    @nro_conta.setter
    def nro_conta(self, nro_conta: int) -> None:
        self._nro_conta = nro_conta
