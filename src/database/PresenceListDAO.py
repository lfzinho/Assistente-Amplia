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

class PresenceListDAO(DataAccessObject):

    