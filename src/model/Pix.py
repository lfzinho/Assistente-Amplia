from model.MetodoPagamento import MetodoPagamento

# testa_informacoes_construtor
# class Pix:
#     def __init__(self, chave:str, tipo:str) -> None:
#         self.chave = chave
#         self.tipo = tipo


# testa_heranca_metodo_pagamento
class Pix(MetodoPagamento):
    def __init__(self, chave:str, tipo:str) -> None:
        self.chave = chave
        self.tipo = tipo

    def visualizar_informacoes(self):
        pass
