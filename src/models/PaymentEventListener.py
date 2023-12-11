from src.models.EventListener import EventListener

class DataAccessObject:
    pass

class PaymentEventListener(EventListener):
    """Classe responsável por ouvir eventos de pagamento."""
    def __init__(self) -> None:
        """Construtor padrão da classe PaymentEventListener."""
        pass

    def update(self, event: dict) -> None:
        """Método responsável por atualizar o estado do
        objeto PaymentEventListener."""
        dao = DataAccessObject(
            'payment-log'
        )
        dao.add(event)

from src.database.DAOFactory import DataAccessObject
