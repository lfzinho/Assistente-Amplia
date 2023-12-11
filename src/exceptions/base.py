# from abc import ABC, abstractmethod
from typing import Union

# class BaseError(ABC, Exception):
#     def __init__(self, msg: str | None = None) -> None:
#         msg = msg or self.message()
#         super().__init__(msg)

#     @abstractmethod
#     def message(self) -> str:
#         ...


class BaseError(Exception):
    """Classe base para outras exceções de mensagem padronizada."""
    def __new__(cls, *args, **kwargs) -> 'BaseError':
        """
        Impede que a classe seja instanciada sem implementar o método
        abstrato, pois a herança de ABC é incompatível com Exception.
        """
        if cls.message == BaseError.message:
            raise TypeError(
                f'A classe "{cls.__name__}" não implementa o método message.'
            )
        return super().__new__(cls)

    def __init__(self, msg: Union[str, None] = None, *args) -> None:
        """
        Inicializa a exceção com a mensagem passada, se houver, ou
        com a mensagem padrão da classe.

        Parâmetros
        ----------
        msg : str, opcional
            Mensagem de erro.
        *args
            Argumentos adicionais para Exception.
        """
        msg = msg or self.message()
        super().__init__(msg, *args)

    def message(self) -> str:
        ...
