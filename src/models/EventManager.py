from abc import ABC, abstractmethod

from src.models.EventListener import EventListener


# class EventManager:
#     """Classe responsável por gerenciar o padrão de projeto Observer."""

#     def __init__(self) -> None:
#         self.listeners = []


# class EventManager:
#     """Classe responsável por gerenciar o padrão de projeto Observer."""

#     def __init__(self) -> None:
#         self.listeners = []

#     def add_listener(self, listener: EventListener) -> None:
#         """Método responsável por adicionar um listener."""
#         self.listeners.append(listener)


# class EventManager:
#     """Classe responsável por gerenciar o padrão de projeto Observer."""

#     def __init__(self) -> None:
#         self.listeners = []

#     def add_listener(self, listener: EventListener) -> None:
#         """Método responsável por adicionar um listener."""
#         self.listeners.append(listener)

#     def remove_listener(self, listener: EventListener) -> None:
#         """Método responsável por remover um listener."""
#         self.listeners.remove(listener)


# class EventManager:
#     """Classe responsável por gerenciar o padrão de projeto Observer."""

#     def __init__(self) -> None:
#         self.listeners = []

#     def add_listener(self, listener: EventListener) -> None:
#         """Método responsável por adicionar um listener."""
#         self.listeners.append(listener)

#     def remove_listener(self, listener: EventListener) -> None:
#         """Método responsável por remover um listener."""
#         self.listeners.remove(listener)

#     def notify(self, event: str) -> None:
#         """Método responsável por notificar os listeners."""
#         for listener in self.listeners:
#             listener.update(event)


class EventManager(ABC):
    """Classe responsável por gerenciar o padrão de projeto Observer."""

    def __init__(self) -> None:
        self.listeners = []

    def add_listener(self, listener: EventListener) -> None:
        """Método responsável por adicionar um listener."""
        self.listeners.append(listener)

    def remove_listener(self, listener: EventListener) -> None:
        """Método responsável por remover um listener."""
        self.listeners.remove(listener)

    def notify(self, event: str) -> None:
        """Método responsável por notificar os listeners."""
        for listener in self.listeners:
            listener.update(event)
