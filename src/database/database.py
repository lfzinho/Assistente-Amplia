import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

import firebase_admin
from firebase_admin import credentials, firestore

# cred = credentials.Certificate("src/database/serviceAccountKey.json")

# app = firebase_admin.initialize_app(cred)
# db = firestore.client()


# class DatabaseManager():
#     def __init__(self, db: firestore.client):
#         self.db = db

#     @staticmethod
#     def instance():
#         return DatabaseManager(db)

#     def get_all(self, collection):
#         docs = self.db.collection(collection).get()
#         return [doc.to_dict() for doc in docs]

#     def get_all_keys(self, collection):
#         docs = self.db.collection(collection).list_documents()
#         return [doc.id for doc in docs]

#     def get_by_id(self, collection, id):
#         doc = self.db.get_by_id(collection, id)
#         return doc.to_dict()

#     def add(self, collection, data):
#         print(collection, data)
#         self.db.collection(collection).add(data)

#     def update(self, collection, id, data):
#         self.db.collection(collection).document(id).set(data)

#     def delete(self, collection, id):
#         self.db.collection(collection).document(id).delete()


class DatabaseManager():
    """Singleton para gerenciar o banco de dados"""
    _instance = None

    def __init__(self):
        if DatabaseManager._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            cred = credentials.Certificate("serviceAccountKey.json")
            firebase_admin.initialize_app(cred)
            self.db = firestore.client()
            DatabaseManager._instance = self

    @staticmethod
    def instance():
        """Retorna a instância do singleton"""
        if not DatabaseManager._instance:
            DatabaseManager._instance = DatabaseManager()
        return DatabaseManager._instance

    def get_all(self, collection):
        """
        Retorna todos os documentos de uma coleção.
        
        Parameters
        ----------
        collection : str
            Nome da coleção do banco de dados.
            
        Returns
        -------
        list
            Lista com os documentos.
        """
        docs = self.db.collection(collection).get()
        return [doc.to_dict() for doc in docs]

    def get_all_keys(self, collection):
        """
        Retorna todos os IDs dos documentos de uma coleção.
        
        Parameters
        ----------
        collection : str
            Nome da coleção do banco de dados.
        
        Returns
        -------
        list
            Lista com os IDs dos documentos."""
        docs = self.db.collection(collection).list_documents()
        return [doc.id for doc in docs]

    def get_by_id(self, collection, id):
        """
        Retorna um documento do banco de dados.
        
        Parameters
        ----------
        collection : str
            Nome da coleção do banco de dados.
        id : str
            ID do documento a ser retornado.
        
        Returns
        -------
        dict
            Dicionário com os dados do documento."""
        doc = self.db.get_by_id(collection, id)
        return doc.to_dict()

    def add(self, collection, data):
        """
        Adiciona um documento ao banco de dados.

        Parameters
        ----------
        collection : str
            Nome da coleção do banco de dados.
        data : dict
            Dados a serem adicionados.
        
        Returns
        -------
        str
            ID do documento adicionado.
        """
        return self.db.collection(collection).add(data)

    def update(self, collection, id, data):
        """
        Atualiza um documento do banco de dados.
        
        Parameters
        ----------
        collection : str
            Nome da coleção do banco de dados.
        id : str
            ID do documento a ser atualizado.
        data : dict
            Dados a serem atualizados.
            
        Returns
        -------
        bool
            True se o documento foi atualizado com sucesso, 
            False caso contrário.
        """
        return self.db.collection(collection).document(id).update(data)

    def delete(self, collection, id):
        """
        Deleta um documento do banco de dados.

        Parameters
        ----------
        collection : str
            Nome da coleção do banco de dados.
        id : str
            ID do documento a ser deletado.
        
        Returns
        -------
        bool
            True se o documento foi deletado com sucesso, 
            False caso contrário.
        """
        return self.db.collection(collection).document(id).delete()
