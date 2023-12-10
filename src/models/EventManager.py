from src.models.EventListener import EventListener


# class EventManager:
#     """Classe responsável por gerenciar o padrão de projeto Observer."""

#     def __init__(self) -> None:
#         self.listeners = []


class EventManager:
    """Classe responsável por gerenciar o padrão de projeto Observer."""

    def __init__(self) -> None:
        self.listeners = []

    def add_listener(self, listener: EventListener) -> None:
        """Método responsável por adicionar um listener."""
        self.listeners.append(listener)

    def remove_listener(self, listener: EventListener) -> None:
        """Método responsável por remover um listener."""
        self.listeners.remove(listener)
