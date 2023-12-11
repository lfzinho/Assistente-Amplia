# Administrator, Analyst, BankAccount, Beneficiary, Cash, Director,
# Payment, Pix, Student, Teacher

from .DataAccessObject import DataAccessObject

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


class PresenceListDAO(DataAccessObject):
    pass
