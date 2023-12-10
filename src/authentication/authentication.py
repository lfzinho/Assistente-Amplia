

from typing import Any
import requests
import json

from firebase_admin import auth

from src.database.database import DatabaseManager

# RED
# from typing import Any

# import firebase_admin
# from firebase_admin import credentials, auth

# import requests
# import json

# cred = credentials.Certificate("serviceAccountKey.json")
# firebase_admin.initialize_app(cred)

# class Authentication():
#     """Classe para gerenciar a autenticação do usuário"""
#     def __init__(self):
#         self.auth = auth
#         self.uid = None

#     def create_user(self, email: str, password: str) -> Any:
#         """Cria um usuário no banco de dados"""
#         self.uid = self.auth.create_user(email=email, password=password).uid
#         return self.uid

#     def get_user_by_email(self, email: str) -> str:
#         """Retorna um usuário do banco de dados"""
#         return self.auth.get_user_by_email(email)

#     def update_user_password(self, uid: str, password: str) -> None:
#         """Atualiza a senha de um usuário no banco de dados"""
#         self.auth.update_user(uid, password=password)

#     def update_user_email(self, uid: str, email: str) -> None:
#         """Atualiza o email de um usuário no banco de dados"""
#         self.auth.update_user(uid, email=email)

#     def delete_user(self, uid: str) -> None:
#         """Deleta um usuário do banco de dados"""
#         self.auth.delete_user(uid)
#         self.uid = None

#     def get_all_users(self):
#         """Retorna todos os usuários do banco de dados"""
#         return self.auth.list_users()

#     def authenticate(self, email: str, password: str) -> bool:
#         """Autentica um usuário no banco de dados"""
#         payload = {
#             "email": email,
#             "password": password,
#             "returnSecureToken": True
#         }

#         with open("serviceAccountKey.json") as f:
#             key = json.load(f)["api_web_key"]
#         response = requests.post(
#             "https://identitytoolkit.googleapis.com/"
#             "v1/accounts:signInWithPassword",
#             params={"key": key},
#             data=payload
#         )

#         if response.status_code == 200:
#             data = response.json()
#             self.uid = data.get("localId")
#             return True
#         else:
#             return False


class Authentication():
    """Classe para gerenciar a autenticação do usuário."""
    def __init__(self):
        self.auth = auth
        self.uid = None
        self.db = DatabaseManager.instance()

    def create_user(self, email: str, password: str) -> Any:
        """Cria um usuário no banco de dados."""
        self.uid = self.auth.create_user(email=email, password=password).uid
        return self.uid

    def get_user_by_uid(self, uid: str) -> str:
        """Retorna um usuário do banco de dados."""
        return self.auth.get_user(uid)

    def get_user_by_email(self, email: str) -> str:
        """Retorna um usuário do banco de dados."""
        return self.auth.get_user_by_email(email)

    def update_user_password(self, uid: str, password: str) -> None:
        """Atualiza a senha de um usuário no banco de dados."""
        self.auth.update_user(uid, password=password)

    def update_user_email(self, uid: str, email: str) -> None:
        """Atualiza o email de um usuário no banco de dados."""
        self.auth.update_user(uid, email=email)

    def delete_user(self, uid: str) -> None:
        """Deleta um usuário do banco de dados."""
        self.auth.delete_user(uid)
        self.uid = None

    def get_all_users(self):
        """Retorna todos os usuários do banco de dados."""
        return self.auth.list_users()

    def authenticate(self, email: str, password: str) -> bool:
        """Autentica um usuário no banco de dados."""
        payload = {
            "email": email,
            "password": password,
            "returnSecureToken": True
        }

        with open("serviceAccountKey.json") as f:
            key = json.load(f)["api_web_key"]
        response = requests.post(
            "https://identitytoolkit.googleapis.com/"
            "v1/accounts:signInWithPassword",
            params={"key": key},
            data=payload
        )

        if response.status_code == 200:
            data = response.json()
            self.uid = data.get("localId")
            return True
        else:
            return False
