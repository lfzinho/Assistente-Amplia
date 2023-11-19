from model.MetodoPagamento import MetodoPagamento

TIPOS_PIX = ['cpf', 'cnpj', 'email', 'celular']

# testa_informacoes_construtor
# class Pix:
#     def __init__(self, chave:str, tipo:str) -> None:
#         self.chave = chave
#         self.tipo = tipo


# testa_heranca_metodo_pagamento
#class Pix(MetodoPagamento):
    # def __init__(self, chave:str, tipo:str) -> None:
    #     self.chave = chave
    #     self.tipo = tipo

    # def visualizar_informacoes(self):
    #    pass

# testa_tipo_retorno_metodo_pagamento
# class Pix(MetodoPagamento):
#     def __init__(self, chave:str, tipo:str) -> None:
#         self.chave = chave
#         self.tipo = tipo

#     def visualizar_informacoes(self):
#         return f"Chave: {self.chave}\nTipo: {self.tipo}"
    
# testa_getters
# class Pix(MetodoPagamento):
#     def __init__(self, chave:str, tipo:str) -> None:
#         self._chave = chave
#         self._tipo = tipo

#     def visualizar_informacoes(self):
#         return f"Chave: {self.chave}\nTipo: {self.tipo}"
    
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

# testa_limitacao_tipo
class Pix(MetodoPagamento):
    """Classe que representa um método de pagamento Pix"""
    def __init__(self, chave:str, tipo:str) -> None:
        """Construtor da classe Pix
        
        Args:
            chave (str): Chave Pix
            tipo (str): Tipo da chave Pix
            
        Raises:
            ValueError: Se o tipo não for  ['cpf', 'cnpj', 'email', 'celular']
        """
        self._tipo = tipo
        self._chave = chave

    def visualizar_informacoes(self):
        """
        Retorna uma string com as informações do Pix
        
        Returns:
            str: Informações do Pix
        """
        return f"Chave: {self.chave}\nTipo: {self.tipo}"
    
    @property
    def tipo(self)-> str:
        """getter do Tipo da chave Pix
            
        Returns:
            str: Tipo da chave Pix
        """
        return self._tipo

    @tipo.setter
    def tipo(self, tipo:str)-> None:
        """setter do Tipo da chave Pix

        Args:
            tipo (str): Tipo da chave Pix

        Raises:
            ValueError: Se o tipo não for  ['cpf', 'cnpj', 'email', 'celular']
        """
        if tipo not in TIPOS_PIX:
            raise ValueError('Tipo inválido, escolha entre: cpf, cnpj, email, celular')
        self._tipo = tipo

    @property
    def chave(self)-> str:
        """getter da Chave Pix
        
        Returns:
            str: Chave Pix
        """
        return self._chave

    @chave.setter
    def chave(self, chave)-> None:
        """setter da sChave Pix
        
        Args:
            chave (str): Chave Pix
        """
        self._chave = chave

    