from typing import Any

import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud.firestore import Client

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


# class DatabaseManager():
#     """Singleton para gerenciar o banco de dados"""
#     _instance = None

#     def __init__(self):
#         if DatabaseManager._instance is not None:
#             raise Exception("This class is a singleton!")
#         else:
#             cred = credentials.Certificate("serviceAccountKey.json")
#             firebase_admin.initialize_app(cred)
#             self.db = firestore.client()
#             DatabaseManager._instance = self

#     @staticmethod
#     def instance():
#         """Retorna a instância do singleton"""
#         if not DatabaseManager._instance:
#             DatabaseManager._instance = DatabaseManager()
#         return DatabaseManager._instance

#     def get_all(self, collection):
#         """
#         Retorna todos os documentos de uma coleção.

#         Parameters
#         ----------
#         collection : str
#             Nome da coleção do banco de dados.

#         Returns
#         -------
#         list
#             Lista com os documentos.
#         """
#         doc_keys = self.get_all_keys(collection)
#         docs = self.db.collection(collection).get()
#         return [doc.to_dict() for doc in docs]

#     def get_all_keys(self, collection):
#         """
#         Retorna todos os IDs dos documentos de uma coleção.

#         Parameters
#         ----------
#         collection : str
#             Nome da coleção do banco de dados.

#         Returns
#         -------
#         list
#             Lista com os IDs dos documentos."""
#         docs = self.db.collection(collection).list_documents()
#         return [doc.id for doc in docs]

#     def get_by_id(self, collection, id):
#         """
#         Retorna um documento do banco de dados.

#         Parameters
#         ----------
#         collection : str
#             Nome da coleção do banco de dados.
#         id : str
#             ID do documento a ser retornado.

#         Returns
#         -------
#         dict
#             Dicionário com os dados do documento."""
#         doc = self.db.get_by_id(collection, id)
#         return doc.to_dict()

#     def add(self, collection, data):
#         """
#         Adiciona um documento ao banco de dados.

#         Parameters
#         ----------
#         collection : str
#             Nome da coleção do banco de dados.
#         data : dict
#             Dados a serem adicionados.

#         Returns
#         -------
#         str
#             ID do documento adicionado.
#         """
#         return self.db.collection(collection).add(data)

#     def update(self, collection, id, data):
#         """
#         Atualiza um documento do banco de dados.

#         Parameters
#         ----------
#         collection : str
#             Nome da coleção do banco de dados.
#         id : str
#             ID do documento a ser atualizado.
#         data : dict
#             Dados a serem atualizados.

#         Returns
#         -------
#         bool
#             True se o documento foi atualizado com sucesso,
#             False caso contrário.
#         """
#         return self.db.collection(collection).document(id).update(data)

#     def delete(self, collection, id):
#         """
#         Deleta um documento do banco de dados.

#         Parameters
#         ----------
#         collection : str
#             Nome da coleção do banco de dados.
#         id : str
#             ID do documento a ser deletado.

#         Returns
#         -------
#         bool
#             True se o documento foi deletado com sucesso,
#             False caso contrário.
#         """
#         return self.db.collection(collection).document(id).delete()


# class DatabaseManager():
#     """Singleton para gerenciar o banco de dados"""
#     _instance = None

#     def __init__(self):
#         if DatabaseManager._instance is not None:
#             raise Exception("This class is a singleton!")
#         else:
#             cred = credentials.Certificate("serviceAccountKey.json")
#             firebase_admin.initialize_app(cred)
#             self.db = firestore.client()
#             DatabaseManager._instance = self

#     @staticmethod
#     def instance():
#         """Retorna a instância do singleton"""
#         if not DatabaseManager._instance:
#             DatabaseManager._instance = DatabaseManager()
#         return DatabaseManager._instance

#     def get_all(self, collection):
#         """
#         Retorna todos os documentos de uma coleção.

#         Parameters
#         ----------
#         collection : str
#             Nome da coleção do banco de dados.

#         Returns
#         -------
#         dict
#             Dicionário com os documentos.
#         """
#         docs = self.db.collection(collection).get()
#         return {doc.id: doc.to_dict() for doc in docs if doc.id != "index"}

#     def get_all_keys(self, collection):
#         """
#         Retorna todos os IDs dos documentos de uma coleção.

#         Parameters
#         ----------
#         collection : str
#             Nome da coleção do banco de dados.

#         Returns
#         -------
#         list
#             Lista com os IDs dos documentos.
#         """
#         docs = self.db.collection(collection).list_documents()
#         return [doc.id for doc in docs if doc.id != "index"]

#     def get_by_id(self, collection, id):
#         """
#         Retorna um documento do banco de dados.

#         Parameters
#         ----------
#         collection : str
#             Nome da coleção do banco de dados.
#         id : str
#             ID do documento a ser retornado.

#         Returns
#         -------
#         dict
#             Dicionário com os dados do documento."""
#         doc = self.db.collection(collection).document(id).get()
#         return doc.to_dict()

#     def add(self, collection, data):
#         """
#         Adiciona um documento ao banco de dados.

#         Parameters
#         ----------
#         collection : str
#             Nome da coleção do banco de dados.
#         data : dict
#             Dados a serem adicionados.

#         Returns
#         -------
#         str
#             ID do documento adicionado.
#         """
#         # get index counter
#         index_query = self.db.collection(collection).document("index").get()
#         if index_query.exists:
#             index = index_query.to_dict()["index"]
#             self.db.collection(collection).document("index")\
#                                           .update({"index": index + 1})
#         else:
#             index = 0
#             self.db.collection(collection).document("index")\
#                                           .set({"index": 1})
#         # add document
#         return self.db.collection(collection).document(str(index)).set(data)

#     def update(self, collection, id, data):
#         """
#         Atualiza um documento do banco de dados.

#         Parameters
#         ----------
#         collection : str
#             Nome da coleção do banco de dados.
#         id : str
#             ID do documento a ser atualizado.
#         data : dict
#             Dados a serem atualizados.

#         Returns
#         -------
#         bool
#             True se o documento foi atualizado com sucesso,
#             False caso contrário.
#         """
#         return self.db.collection(collection).document(id).update(data)

#     def delete(self, collection, id):
#         """
#         Deleta um documento do banco de dados.

#         Parameters
#         ----------
#         collection : str
#             Nome da coleção do banco de dados.
#         id : str
#             ID do documento a ser deletado.

#         Returns
#         -------
#         bool
#             True se o documento foi deletado com sucesso,
#             False caso contrário.
#         """
#         return self.db.collection(collection).document(id).delete()


class DatabaseManager():
    """Singleton para gerenciar o banco de dados."""
    _instance = None

    def __init__(self) -> None:
        if DatabaseManager._instance is not None:
            raise RuntimeError("This class is a singleton!")
        else:
            cred = credentials.Certificate("serviceAccountKey.json")
            firebase_admin.initialize_app(cred)
            self.db: Client = firestore.client()
            DatabaseManager._instance = self

    @staticmethod
    def instance() -> "DatabaseManager":
        """Retorna a instância do singleton."""
        if not DatabaseManager._instance:
            DatabaseManager._instance = DatabaseManager()
        return DatabaseManager._instance

    def get_all(self, collection: str) -> dict[str, Any]:
        """
        Retorna todos os documentos de uma coleção.

        Parameters
        ----------
        collection : str
            Nome da coleção do banco de dados.

        Returns
        -------
        dict
            Dicionário com os documentos.
        """
        docs = self.db.collection(collection).get()
        return {doc.id: doc.to_dict() for doc in docs if doc.id != "index"}

    def get_all_keys(self, collection: str) -> list[str]:
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
        docs = self.db.collection(collection).list_documents()
        return [doc.id for doc in docs if doc.id != "index"]

    def get_by_id(self, collection: str, id: str) -> Any:
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
        doc = self.db.collection(collection).document(id).get()
        return doc.to_dict()

    def add(self, collection: str, data: dict[str, Any]) -> str:
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
        # get index counter
        index_query = self.db.collection(collection).document("index").get()
        if index_query.exists:
            index = index_query.to_dict()["index"]
            self.db.collection(collection).document("index")\
                                          .update({"index": index + 1})
        else:
            index = 0
            self.db.collection(collection).document("index")\
                                          .set({"index": 1})
        # add document
        return self.db.collection(collection).document(str(index)).set(data)

    def update(self, collection: str, id: str, data: dict[str, Any]) -> None:
        """
        Atualiza um documento do banco de dados.

        Parameters
        ----------
        collection : str
            Nome da coleção do banco de dados.
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
        return self.db.collection(collection).document(id).update(data)

    def delete(self, collection: str, id: str) -> bool:
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
        if not self.db.collection(collection).document(id).get().exists:
            return False
        self.db.collection(collection).document(id).delete()
        return True
