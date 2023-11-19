from abc import ABC, abstractmethod

class MetodoPagamento(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def visualizar_informacoes(self):
        pass
