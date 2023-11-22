from typing import Type

from src.models.Pessoa import Pessoa

from datetime import date
from src.models.MetodoPagamento import MetodoPagamento

# testa_heraca_pessoa
class Professor(Pessoa):
    pass

# testa_construtor
# class Professor(Pessoa):

#     def __init__(
#             self,
#             nome: str,
#             data_nascimento: date,
#             cpf: str,
#             endereco: str,
#             metodo_pagamento: type[MetodoPagamento]
#         ) -> None:

#         super().__init__(nome, data_nascimento, cpf, endereco, metodo_pagamento)

# testa_atributo salário
class Professor(Pessoa):

    def __init__(
            self,
            nome: str,
            data_nascimento: date,
            cpf: str,
            endereco: str,
            metodo_pagamento: type[MetodoPagamento],
            salario: float
        ) -> None:

        super().__init__(nome, data_nascimento, cpf, endereco, metodo_pagamento)
        self._salario = salario

    @property
    def salario(self) -> float:
        return self._salario
    
    @salario.setter
    def salario(self, novo_salario: float) -> None:
        
        self._salario = novo_salario
    
