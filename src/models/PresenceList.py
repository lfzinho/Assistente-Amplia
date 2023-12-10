from datetime import date
from typing import Optional, Type

from src.models.Beneficiary import Beneficiary
from src.models.PaymentMethod import PaymentMethod

class PresenceList:
    def __init__(
        self,
        class_date: date,
        presence_ids: list[int],
    ) -> None:
        if not isinstance(class_date, date):
            class_date = date.fromisoformat(class_date)
        self.class_date = class_date
        if any([not isinstance(presence_id, int) for presence_id in
            presence_ids]):
            raise ValueError("presence_ids deve ser uma lista de " +
                "inteiros")
        if len(presence_ids) != len(set(presence_ids)):
            raise ValueError("presence_ids não pode conter valores " +
                "repetidos")
        self.presence_ids = presence_ids

