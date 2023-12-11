import io
from typing import Any

import pandas as pd

from src.exceptions.data_input import InvalidCSV
# Adaptee
from src.interface.forms.base_forms import CreationForm
from src.interface.forms.fields import Field, SelectBoxField


class CSV(CreationForm):
    """
    Adaptador para dados inseridos por arquivo CSV em vez de
    entrada direta no formulário.

    Atributos
    ---------
    df : pandas.DataFrame
        DataFrame com os dados do arquivo CSV.
    index : int
        Índice da linha atual do arquivo CSV.
    """
    def __init__(
        self,
        file_data: io.BytesIO,
        title: str,
        description: str,
        fields: list[Field]
    ) -> None:
        super().__init__(title, description, fields, 'payment')
        try:
            self.df = pd.read_csv(
                file_data, header=None, skiprows=2, parse_dates=[0, 1]
            ).iloc[:, :3]
        except Exception:
            raise InvalidCSV()
        self.index = 0

    def _money_to_float(self, value: str) -> float:
        """Converte uma string formatada em reais para float."""
        if isinstance(value, float):
            return value
        return float(
            value
                .removeprefix('R$')
                .strip()
                .replace(',', '.')
        )

    def get_form_values(self) -> dict[str, Any]:
        """
        Obtém um dicionário que descreve a instância de pagamento
        representada por cada linha do CSV e avança o índice.

        Ao final da iteração, retorna um dicionário vazio.

        Retorna
        -------
        dict[str, Any]
            Dicionário com os valores do formulário.
        """
        if self.index >= len(self.df):
            return {}
        form_values = {'class_name': 'Payment'}
        try:
            # Obtém apenas as linhas referentes ao pagamento
            row = self.df.iloc[self.index]
            self.index += 1
            values = row.to_list()
            form_values['reference_date'] = values[0].to_pydatetime()
            form_values['payment_date'] = values[1].to_pydatetime()
            form_values['value'] = self._money_to_float(values[2])
        except Exception:
            raise InvalidCSV()
        return form_values
