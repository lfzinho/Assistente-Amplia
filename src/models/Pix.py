from typing import Literal

from src.models.MetodoPagamento import MetodoPagamento

TIPOS_PIX = ['cpf', 'cnpj', 'email', 'celular']


# class Pix:
#     def __init__(self, chave:str, tipo:str) -> None:
#         self.chave = chave
#         self.tipo = tipo


#class Pix(MetodoPagamento):
    # def __init__(self, chave:str, tipo:str) -> None:
    #     self.chave = chave
    #     self.tipo = tipo

    # def visualizar_informacoes(self):
    #    pass


# class Pix(MetodoPagamento):
#     def __init__(self, chave:str, tipo:str) -> None:
#         self.chave = chave
#         self.tipo = tipo

#     def visualizar_informacoes(self):
#         return f'Chave: {self.chave}\nTipo: {self.tipo}'

# class Pix(MetodoPagamento):
#     def __init__(self, chave:str, tipo:str) -> None:
#         self._chave = chave
#         self._tipo = tipo

#     def visualizar_informacoes(self):
#         return f'Chave: {self.chave}\nTipo: {self.tipo}"

#     @property
#     def chave(self):
#         return self._chave

#     @chave.setter
#     def chave(self, chave):
#         self._chave = chave

#     @property
#     def tipo(self):
#         return self._tipo

#     @tipo.setter
#     def tipo(self, tipo):
#         self._tipo = tipo


class Pix(MetodoPagamento):
    """Classe que representa um método de pagamento Pix."""
    def __init__(
        self, chave: str, tipo: Literal['cpf', 'cnpj', 'email', 'celular']
    ) -> None:
        """
        Construtor da classe Pix.

        Parâmetros
        ----------
        chave : str
            Chave Pix.
        tipo : {'cpf', 'cnpj', 'email', 'celular'}
            Tipo da chave Pix.

        Levanta
        -------
        ValueError
            Se o tipo não for um de {'cpf', 'cnpj', 'email', 'celular'}.
        """
        self._tipo = tipo
        self._chave = chave

    def visualizar_informacoes(self) -> str:
        """
        Retorna uma string com as informações do Pix.

        Retorna
        -------
        str
            Informações do Pix.
        """
        return f'Chave: {self.chave}\nTipo: {self.tipo}'

    @property
    def tipo(self) -> str:
        """
        Getter do tipo da chave Pix.

        Retorna
        -------
        str
            Tipo da chave Pix.
        """
        return self._tipo

    @tipo.setter
    def tipo(self, tipo: str) -> None:
        """
        Parâmetros
        ----------
        tipo : str
            Tipo da chave Pix.

        Levanta
        -------
        ValueError
            Se o tipo não for um de {'cpf', 'cnpj', 'email', 'celular'}.
        """
        if tipo not in TIPOS_PIX:
            raise ValueError(
                'Tipo inválido, escolha entre: cpf, cnpj, email, celular'
            )
        self._tipo = tipo

    @property
    def chave(self) -> str:
        """
        Getter da Chave Pix.

        Retorna
        -------
        str
            Chave Pix.
        """
        return self._chave

    @chave.setter
    def chave(self, chave)-> None:
        """
        Setter da Chave Pix.

        Parâmetros
        ----------
        chave : str
            Chave Pix.
        """
        self._chave = chave
