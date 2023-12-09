from datetime import date
from typing import Literal, Optional, Type

from src.models.Analyst import Analyst
from src.models.Person import Person
from src.models.PaymentMethod import PaymentMethod


class Director(Analyst):
    def __init__(self, name, email, cpf, address, payment_method,
        birth_date, admission_date, occupation_area,
        office_admission_date, office_exit_date=None, exit_date=None):
        super().__init__(name, email, cpf, address, payment_method,
        birth_date, admission_date, occupation_area, exit_date)
        # Checa admission_date < office_admission_date
        if office_admission_date < admission_date:
            raise ValueError("""A data de promoção não pode ser anterior
                à data de admissão""")
        # Checa office_exit_date < office_admission_date
        if office_exit_date is not None:
            if office_exit_date < office_admission_date:
                raise ValueError("""A data de saída do cargo não pode
                    ser anterior à data de entrada""")
        self.office_admission_date = office_admission_date
        self.office_exit_date = office_exit_date
