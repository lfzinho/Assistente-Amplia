import sys
import os
from abc import ABC, abstractmethod

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

    def __init__(self, collection, class_):
        self.dbm = DatabaseManager.instance()
        self.collection = collection
        self.class_ = class_

    def get_all_data(self):
        return self.dbm.get_all(self.collection)

    def get_all_obj(self):
        docs = self.dbm.get_all(self.collection)
        return {doc.id: self.class_.from_data(**doc.to_dict()) for doc in
            docs if doc.id != 'index'}

    def get_all_keys(self):
        return self.dbm.get_all_keys(self.collection)

    def get_data_by_id(self, id_value):
        return self.dbm.get_by_id(self.collection, id_value)

    def get_obj_by_id(self, id_value):
        doc_dict = self.dbm.get_by_id(self.collection, id_value)
        return self.from_data(**doc_dict)

    def add(self, obj):
        data = self.to_data(obj)
        return self.dbm.add(self.collection, data)

    def update(self, id_value, data):
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
        return self.dbm.delete(self.collection, id_value)
