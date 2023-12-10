from src.models.EventListener import EventListener

class PaymentEventListener(EventListener):
    """Classe responsável por ouvir eventos de pagamento."""
    def __init__(self) -> None:
        """Construtor padrão da classe PaymentEventListener."""
        self.listeners = []

    def update(self, event) -> None:
        """Método responsável por atualizar o estado do
        objeto PaymentEventListener."""
        self.event = event
