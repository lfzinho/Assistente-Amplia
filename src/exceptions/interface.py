from .base import BaseError


class NoIdError(BaseError):
    """Exceção para formulários sem campo de ID."""
    def message(self) -> str:
        return 'O formulário não possui um campo de ID.'
