from model.MetodoPagamento import MetodoPagamento

class Pix(MetodoPagamento):
    def __init__(self, chave:str, tipo:str) -> None:
        self.chave = chave
        self.tipo = tipo