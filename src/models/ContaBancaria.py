from src.models.MetodoPagamento import MetodoPagamento

# testa_informacoes_construtor
# class ContaBancaria:

#     def __init__(self, banco:str, agencia:int, nro_conta:int) -> None:
#         self._banco = banco
#         self._agencia = agencia
#         self._nro_conta = nro_conta

# testa_heranca_metodo_pagamento
# class ContaBancaria(MetodoPagamento):

#     def __init__(self, banco:str, agencia:int, nro_conta:int) -> None:
#         self._banco = banco
#         self._agencia = agencia
#         self._nro_conta = nro_conta

#     def visualizar_informacoes(self):
#         pass

# testa_retorno_metodo_pagamento
# class ContaBancaria(MetodoPagamento):

#     def __init__(self, banco:str, agencia:int, nro_conta:int) -> None:
#         self._banco = banco
#         self._agencia = agencia
#         self._nro_conta = nro_conta

#     def visualizar_informacoes(self):
#         return f"Banco: {self._banco}\nAgência: {self._agencia}\nNúmero da conta: {self._nro_conta}"
    
# testa_getters e setters
class ContaBancaria(MetodoPagamento):

    def __init__(self, banco:str, agencia:int, nro_conta:int) -> None:
        self._banco = banco
        self._agencia = agencia
        self._nro_conta = nro_conta

    def visualizar_informacoes(self):
        return f"Banco: {self._banco}\nAgência: {self._agencia}\nNúmero da conta: {self._nro_conta}"
    
    @property
    def banco(self):
        return self._banco
    
    @banco.setter
    def banco(self, banco):
        self._banco = banco

    @property
    def agencia(self):
        return self._agencia
    
    @agencia.setter
    def agencia(self, agencia):
        self._agencia = agencia

    @property
    def nro_conta(self):
        return self._nro_conta
    
    @nro_conta.setter
    def nro_conta(self, nro_conta):
        self._nro_conta = nro_conta
