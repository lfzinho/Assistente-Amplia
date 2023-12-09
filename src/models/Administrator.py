from datetime import date
from typing import Literal, Optional, Type

from src.models.Director import Director
from src.models.PaymentMethod import PaymentMethod


class Administrator(Director):
    def __init__(self, name, email, cpf, address, payment_method,
        birth_date, admission_date, occupation_area,
        office_admission_date, office_exit_date=None, exit_date=None):
        super().__init__(name, email, cpf, address, payment_method,
        birth_date, admission_date, occupation_area, exit_date)
