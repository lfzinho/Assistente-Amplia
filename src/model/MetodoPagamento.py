from abc import ABC, abstractmethod

# código incial
# class MetodoPagamento(ABC):
#     def __init__(self):
#         pass
#
#     def visualizar_informacoes(self):
#         pass

# testa os métodos abstratos
class MetodoPagamento(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def visualizar_informacoes(self):
        pass