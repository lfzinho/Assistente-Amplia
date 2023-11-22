from typing import Type

from src.models.Pessoa import Pessoa

from datetime import date
from src.models.MetodoPagamento import MetodoPagamento


# testa_heraca_pessoa
# class Aluno(Pessoa):
#     pass

# testa_construtor
class Aluno(Pessoa):
    
    def __init__(
            self, 
            nome: str,
            data_nascimento: date,
            cpf: str,
            endereco: str, 
            metodo_pagamento: type[MetodoPagamento]
        ) -> None:
        super().__init__(nome, data_nascimento, cpf, endereco, metodo_pagamento)