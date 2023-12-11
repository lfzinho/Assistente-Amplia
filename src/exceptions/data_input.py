from .base import BaseError


class InvalidCSV(BaseError):
    """Exceção para arquivos CSV no formato inválido."""
    def message(self) -> str:
        return (
            'O arquivo CSV deve possuir as primeiras três colunas '
            'com valores para a data referente, data de pagamento '
            'e o valor do pagamento, respectivamente. As datas devem '
            'seguir o padrão ISO 8601 (AAAA-MM-DD) e o valor deve '
            'ser um número real não negativo.'
        )
