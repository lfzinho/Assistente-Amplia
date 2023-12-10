from datetime import date
from typing import Optional, Type

from src.models.Beneficiary import Beneficiary
from src.models.PaymentMethod import PaymentMethod

# class PresenceList:
#     def __init__(
#         self,
#         class_date: date,
#         presence_ids: list[int],
#     ) -> None:
#         if not isinstance(class_date, date):
#             class_date = date.fromisoformat(class_date)
#         self.class_date = class_date
#         if any([not isinstance(presence_id, int) for presence_id in
#             presence_ids]):
#             raise ValueError("presence_ids deve ser uma lista de " +
#                 "inteiros")
#         if len(presence_ids) != len(set(presence_ids)):
#             raise ValueError("presence_ids não pode conter valores " +
#                 "repetidos")
#         self.presence_ids = presence_ids


class PresenceList:
    def __init__(
        self,
        class_date: date,
        presence_ids: list[int],
    ) -> None:
        """
        Classe que representa uma lista de presença de beneficiários
        para uma aula
        """
        self.class_date = class_date
        self.presence_ids = presence_ids

    @property
    def class_date(self) -> date:
        """Getter da data da aula"""
        return self._class_date

    @class_date.setter
    def class_date(self, class_date: date) -> None:
        """Setter da data da aula"""
        if not isinstance(class_date, date):
            # date.fromisoformat simultaneamente converte o tipo errado e
            # levanta ValueError se o input for invalido
            class_date = date.fromisoformat(class_date)
        self._class_date = class_date

    @property
    def presence_ids(self) -> list[int]:
        """Getter dos ids dos beneficiários presentes"""
        return self._presence_ids

    @presence_ids.setter
    def presence_ids(self, presence_ids: list[int]) -> None:
        """Setter dos ids dos beneficiários presentes"""
        # Checa se todos os ids são inteiros
        if any([not isinstance(presence_id, int) for presence_id in
            presence_ids]):
            raise ValueError("presence_ids deve ser uma lista de " +
                "inteiros")
        # Checa se não há ids repetidos
        if len(presence_ids) != len(set(presence_ids)):
            raise ValueError("presence_ids não pode conter valores " +
                "repetidos")
        self._presence_ids = presence_ids
