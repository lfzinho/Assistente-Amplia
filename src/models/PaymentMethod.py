from abc import ABC, abstractmethod


# class PaymentMethod:
#     def __init__(self):
#         pass

#     def view_information(self):
#         pass


class PaymentMethod(ABC):
    """Classe que representa um método de pagamento."""
    @abstractmethod
    def __init__(self) -> None:
        """
        Construtor da classe PaymentMethod.
        """
        pass

    @abstractmethod
    def get_information(self) -> None:
        """
        Método que retorna as informações do método de pagamento.
        Utilizada pelas classes filhos seguindo o padrão de projeto
        Strategy.
        """
        pass
