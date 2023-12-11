import sys
import os
from abc import ABC, abstractmethod
from datetime import date
from typing import Any

import firebase_admin
from firebase_admin import credentials, firestore

# Administrator, Analyst, BankAccount, Beneficiary, Cash, Director,
# Payment, Pix, Student, Teacher

from src.database.database import DatabaseManager
from src.models.Analyst import Analyst
from src.models.Administrator import Administrator
from src.models.BankAccount import BankAccount
from src.models.Beneficiary import Beneficiary
from src.models.Cash import Cash
from src.models.Director import Director
from src.models.Payment import Payment
from src.models.Pix import Pix
from src.models.Student import Student
from src.models.Teacher import Teacher


sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))


class DataAccessObject():
    """
    Classe para comunicação da interface com o database manager
    """
    def __init__(self, collection: str):
        self.dbm = DatabaseManager.instance()
        self.collection = collection

    @staticmethod
    def is_valid_type(value: Any) -> bool:
        """
        Checa se o valor é de um tipo válido para serialização JSON,
        que é o tipo de dado que o banco de dados aceita.

        Parâmetros
        ----------
        value : Any
            O valor a ser checado.

        Retorna
        -------
        bool
            True se o valor é de um tipo válido.
        """
        if value is None:
            return True
        return isinstance(value, (list, str, int, float, bool,
            date, dict, ))

    @classmethod
    def to_data(cls, obj) -> dict[str, Any]:
        """
        Serializa o objeto para um dicionário.

        Retorna
        -------
        dict[str, Any]
            Mapeamento de nomes de atributos para valores.
        """
        data = {'class_name': obj.__class__.__name__}
        for key, value in obj.__dict__.items():
            # Remove o underscore do início do nome do atributo, para
            # que o atributo seja definido por meio do setter
            key = key.lstrip('_')
            if isinstance(value, date):
                data[key] = value.strftime('%Y-%m-%d')
            elif cls.is_valid_type(value):
                data[key] = value
            else:
                data[key] = cls.to_data(value)

        return data

    @classmethod
    def from_data(cls, data: dict[str, Any]) -> Any:
        """
        Deserializa um dicionário para um objeto.

        Parâmetros
        ----------
        data : dict[str, Any]
            Mapeamento de nomes de atributos para valores.

        Retorna
        -------
        Form
            O objeto deserializado.
        """
        for key, value in data.items():
            if isinstance(value, dict):
                data[key] = cls.from_data(value)
        # Obtém o atributo class_name enquanto
        # o deixa de fora do dicionário de dados
        class_name = data.pop('class_name')
        obj = eval(class_name)(**data)

        return obj

    def get_all_data(self):
        """
        Coleta todas as ocorrências de uma coleção do banco de dados.
        Retorna na forma serializada.
        """
        return self.dbm.get_all(self.collection)

    def get_all_obj(self):
        """
        Coleta todas as ocorrências de uma coleção do banco de dados.
        Retorna na forma de objetos da classe.
        """
        docs = self.dbm.get_all(self.collection)
        return {doc.id: self.from_data(**doc.to_dict()) for doc in
            docs if doc.id != 'index'}

    def get_all_keys(self):
        """
        Retorna todos os IDs dos documentos de uma coleção.

        Parameters
        ----------
        collection : str
            Nome da coleção do banco de dados.

        Returns
        -------
        list[str]
            Lista com os IDs dos documentos.
        """
        return self.dbm.get_all_keys(self.collection)

    def get_data_by_id(self, id_value):
        """
        Retorna um documento do banco de dados.

        Parameters
        ----------
        id : str
            ID do documento a ser retornado.

        Returns
        -------
        dict
            Dicionário com os dados do documento."""
        return self.dbm.get_by_id(self.collection, id_value)

    def get_obj_by_id(self, id_value):
        """
        Retorna um objeto do banco de dados.

        Parameters
        ----------
        id : str
            ID do documento a ser retornado.

        Returns
        -------
        Any
            Objeto com os dados do documento."""
        doc_dict = self.dbm.get_by_id(self.collection, id_value)
        return self.from_data(**doc_dict)

    def add(self, data):
        """
        Adiciona um documento ao banco de dados.

        Parameters
        ----------
        data : dict
            Dados a serem adicionados.

        Returns
        -------
        str
            ID do documento adicionado.
        """
        return self.dbm.add(self.collection, data)

    def update(self, id_value, data):
        """
        Atualiza um documento do banco de dados.

        Parameters
        ----------
        id : str
            ID do documento a ser atualizado.
        data : dict[str, Any]
            Dados a serem atualizados.

        Returns
        -------
        bool
            True se o documento foi atualizado com sucesso,
            False caso contrário.
        """
        obj = self.get_obj_by_id(id_value)

        for key, value in data:
            if value is not None:
                obj.__setattr__(key, value)
        # TODO change 'for' above to this:
        # try:
        #     for key, value in data:
        #         if value is not None:
        #             obj.__setattr__(key, value)
        # except ValueError:
        #     return False

        data = self.to_data(obj)

        return self.dbm.update(self.collection, id_value, data)

    def delete(self, id_value):
        """
        Deleta um documento do banco de dados.

        Parameters
        ----------
        id_value : str
            ID do documento a ser deletado.

        Returns
        -------
        bool
            True se o documento foi deletado com sucesso,
            False caso contrário.
        """
        return self.dbm.delete(self.collection, id_value)
