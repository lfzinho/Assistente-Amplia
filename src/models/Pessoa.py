from datetime import date
from typing import Type
from src.models.MetodoPagamento import MetodoPagamento

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
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco
        self.metodo_pagamento = metodo_pagamento
