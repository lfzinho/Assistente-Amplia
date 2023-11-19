from datetime import date

class Pessoa:
    """Classe que representa uma pessoa"""
    def __init__(
            self, 
            nome:str, 
            data_nascimento:date,
            cpf:str,
            endereco:str
    ) -> None:
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco
