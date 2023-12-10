from datetime import date
from typing import Literal, Optional, Type

from src.models.Analyst import Analyst
from src.models.PaymentMethod import PaymentMethod


# class Director(Analyst):
#     def __init__(self, name, email, cpf, address, payment_method,
#         birth_date, admission_date, occupation_area,
#         office_admission_date, office_exit_date=None, exit_date=None):
#         super().__init__(name, email, cpf, address, payment_method,
#         birth_date, admission_date, occupation_area, exit_date)
#         # Checa admission_date < office_admission_date
#         if office_admission_date < admission_date:
#             raise ValueError("""A data de promoção não pode ser anterior
#                 à data de admissão""")
#         # Checa office_exit_date < office_admission_date
#         if office_exit_date is not None:
#             if office_exit_date < office_admission_date:
#                 raise ValueError("""A data de saída do cargo não pode
#                     ser anterior à data de entrada""")
#         self.office_admission_date = office_admission_date
#         self.office_exit_date = office_exit_date


class Director(Analyst):
    def __init__(
        self,
        name: str,
        email: str,
        cpf: str,
        address: str,
        payment_method: Type[PaymentMethod],
        birth_date: date,
        admission_date: date,
        occupation_area: Literal['Administrativo Financeiro',
        'Recursos Humanos', 'Pedagógico', 'Marketing'],
        office_admission_date: date,
        office_exit_date: Optional[date]=None,
        exit_date: Optional[date] = None,
    ) -> None:
        super().__init__(
            name,
            email,
            cpf,
            address,
            payment_method,
            birth_date,
            admission_date,
            occupation_area,
            exit_date,
        )
        self.office_admission_date = office_admission_date
        self.office_exit_date = office_exit_date
        self.class_ = 'Director'

    @property
    def office_admission_date(self) -> str:
        """Getter da data de promoção do diretor"""
        return self._occupation_area

    @office_admission_date.setter
    def office_admission_date(
        self,
        office_admission_date: date
    ) -> None:
        """Setter da data de promoção do diretor"""
        if office_admission_date < self.admission_date:
            raise ValueError("""A data de promoção não pode ser anterior
                à data de admissão""")
        self._occupation_area = office_admission_date

    @property
    def office_exit_date(self) -> str:
        """Getter da data de saída do cargo do diretor"""
        return self._occupation_area

    @office_exit_date.setter
    def office_exit_date(
        self,
        office_exit_date: date
    ) -> None:
        """Setter da data de saída do cargo do diretor"""
        if office_exit_date is not None:
            if office_exit_date < self.office_admission_date:
                raise ValueError("""A data de saída do cargo não pode
                    ser anterior à data de entrada""")
        self._occupation_area = office_exit_date
