import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("src/database/serviceAccountKey.json")

app = firebase_admin.initialize_app(cred)
db = firestore.client()


class DatabaseManager():
    def __init__(self, db: firestore.client):
        self.db = db

    @staticmethod
    def instance():
        return DatabaseManager(db)

    def get_all(self, collection):
        docs = self.db.collection(collection).get()
        return [doc.to_dict() for doc in docs]

    def get_all_keys(self, collection):
        docs = self.db.collection(collection).list_documents()
        return [doc.id for doc in docs]

    def get_by_id(self, collection, id):
        doc = self.db.get_by_id(collection, id)
        return doc.to_dict()

    def add(self, collection, data):
        print(collection, data)
        self.db.collection(collection).add(data)

    def update(self, collection, id, data):
        self.db.collection(collection).document(id).set(data)

    def delete(self, collection, id):
        self.db.collection(collection).document(id).delete()
