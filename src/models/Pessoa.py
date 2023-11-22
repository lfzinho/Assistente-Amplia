from datetime import date
from typing import Type
from src.models.MetodoPagamento import MetodoPagamento

# testa_informacoes_construtor
# class Pessoa:
#     """Classe que representa uma pessoa"""
#     def __init__(
#             self, 
#             nome:str, 
#             data_nascimento:date,
#             cpf:str,
#             endereco:str,
#             metodo_pagamento:Type[MetodoPagamento]
#     ) -> None:
#         self.nome = nome
#         self.data_nascimento = data_nascimento
#         self.cpf = cpf
#         self.endereco = endereco
#         self.metodo_pagamento = metodo_pagamento

# testa_getters
class Pessoa:
    """Classe que representa uma pessoa"""
    def __init__(
            self, 
            nome:str, 
            data_nascimento:date,
            cpf:str,
            endereco:str,
            metodo_pagamento:Type[MetodoPagamento]
    ) -> None:
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._cpf = cpf
        self._endereco = endereco
        self._metodo_pagamento = metodo_pagamento

    @property
    def nome(self) -> str:
        return self._nome
    
    @property
    def data_nascimento(self) -> date:
        return self._data_nascimento
    
    @property
    def cpf(self) -> str:
        return self._cpf
    
    @property
    def endereco(self) -> str:
        return self._endereco
    
    @property
    def metodo_pagamento(self) -> Type[MetodoPagamento]:
        return self._metodo_pagamento
    
