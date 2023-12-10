from typing import Literal

from src.models.PaymentMethod import PaymentMethod

PIX_TYPES = ['cpf', 'cnpj', 'email', 'celular', 'aleatorio']


# class Pix:
#     def __init__(self, key: str, type_: str) -> None:
#         self.key = key
#         self.type_ = type_


# class Pix(PaymentMethod):
#     def __init__(self, key: str, type_: str) -> None:
#         self.key = key
#         self.type_ = type_

#     def get_information(self):
#         pass


# class Pix(PaymentMethod):
#     def __init__(self, key: str, type_: str) -> None:
#         self.key = key
#         self.type_ = type_

#     def get_information(self):
#         return f'key: {self.key}\ntype_: {self.type_}'


# class Pix(PaymentMethod):
#     def __init__(self, key: str, type_: str) -> None:
#         self.key = key
#         self.type_ = type_

#     def get_information(self):
#         return f'Chave: {self.key}\nTipo: {self.type_}'


# class Pix(PaymentMethod):
#     def __init__(self, key: str, type_: str) -> None:
#         self._key = key
#         self._type_ = type_

#     def get_information(self):
#         return f'Chave: {self.key}\nTipo: {self.type_}'

#     @property
#     def key(self):
#         return self._key

#     @key.setter
#     def key(self, key):
#         self._key = key

#     @property
#     def type_(self):
#         return self._type_

#     @type_.setter
#     def type_(self, type_):
#         self._type_ = type_



class Pix(PaymentMethod):
    """Classe que representa um método de pagamento Pix."""
    def __init__(
        self, key: str, type_: Literal['cpf', 'cnpj', 'email', 'celular']
    ) -> None:
        """
        Construtor da classe Pix.

        Parâmetros
        ----------
        key : str
            Chave Pix.
        type_ : {'cpf', 'cnpj', 'email', 'celular', 'aleatorio'}
            Tipo da chave Pix.

        Levanta
        -------
        ValueError
            Se o tipo não for um de {'cpf', 'cnpj', 'email', 'celular'}.
        """
        self._key = key
        self._type_ = type_

    def get_information(self) -> str:
        """
        Retorna uma string com as informações do Pix.

        Retorna
        -------
        str
            Informações do Pix.
        """
        return f'Chave: {self.key}\nTipo: {self.type_}'

    @property
    def key(self) -> str:
        """
        Getter do tipo da chave Pix.

        Retorna
        -------
        str
            Tipo da chave Pix.
        """
        return self._key

    @key.setter
    def key(self, key: str) -> None:
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
        self._key = key

    @property
    def type_(self) -> str:
        """
        Getter da Chave Pix.

        Retorna
        -------
        str
            Chave Pix.
        """
        return self._type_

    @type_.setter
    def type_(self, type_: str) -> None:
        """
        Setter da Chave Pix.

        Parâmetros
        ----------
        chave : str
            Chave Pix.
        """
        if type_ not in PIX_TYPES:
            raise ValueError(
                f'Tipo inválido. Escolha entre: {PIX_TYPES}'
            )
        self._type_ = type_
