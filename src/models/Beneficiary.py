from abc import ABC, abstractmethod

from src.models.Person import Person


class Beneficiary:
    """Classe que representa um beneficiário."""
    def __init__(self, transport_cost: float, transport_description: str) -> None:
        self.transport_cost = transport_cost
        self.transport_description = transport_description

