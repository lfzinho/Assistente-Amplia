from abc import ABC, abstractmethod

class EventListener(ABC):
    """Classe abstrata responsável por definir um listener de eventos."""
    @abstractmethod
    def update(self, event):
        """Método abstrato responsável por atualizar o listener."""
        pass
