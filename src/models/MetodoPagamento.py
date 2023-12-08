from abc import ABC, abstractmethod


# class MetodoPagamento(ABC):
#     def __init__(self):
#         pass
#
#     def visualizar_informacoes(self):
#         pass


class MetodoPagamento(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def visualizar_informacoes(self):
        pass
