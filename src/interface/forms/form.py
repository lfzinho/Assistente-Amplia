import datetime
from abc import ABC, abstractmethod
from typing import Any

import streamlit as st

from .fields import Field, SelectBoxField
from src.database.database import DatabaseManager
from src.exceptions.interface import NoIdError
# Garante que todos os tipos já tenham sido importados para
# que o eval do método `from_data` funcione corretamente
from src.models.Administrator import Administrator
from src.models.Analyst import Analyst
from src.models.Beneficiary import Beneficiary
from src.models.Cash import Cash
from src.models.Director import Director
from src.models.Payment import Payment
from src.models.BankAccount import BankAccount
from src.models.PaymentMethod import PaymentMethod
from src.models.Pix import Pix


class Form(ABC):

    def __init__(
        self,
        title: str,
        description: str,
        fields: list[Field],
        id_field: SelectBoxField | None = None,
        db_collection: str | None = None
    ) -> None:
        self.title = title
        self.description = description
        self.fields = fields
        self.id_field = id_field
        self.db_collection = db_collection

        self.db_manager = DatabaseManager.instance()

    @staticmethod
    def is_valid_type(value: Any) -> bool:
        """
        Checa se o valor é de um tipo válido para serialização JSON,
        que é o tipo de dado que o banco de dados aceita.

        Parâmetros
        ----------
        value : Any
            O valor a ser checado.

        Retorna
        -------
        bool
            True se o valor é de um tipo válido.
        """
        if value is None:
            return True
        return isinstance(value, (list, str, int, float, bool,
            datetime.date, dict, ))

    def to_data(self) -> dict[str, Any]:
        """
        Serializa o objeto para um dicionário.

        Retorna
        -------
        dict[str, Any]
            Mapeamento de nomes de atributos para valores.
        """
        data = {'class_name': self.__class__.__name__}
        for key, value in self.__dict__.items():
            # Remove o underscore do início do nome do atributo, para
            # que o atributo seja definido por meio do setter
            key = key.lstrip('_')
            if isinstance(value, datetime.date):
                data[key] = value.strftime('%Y-%m-%d')
            elif self.is_valid_type(value):
                data[key] = value
            else:
                data[key] = Form.to_data(value)

        return data

    @staticmethod
    def from_data(data: dict[str, Any]) -> 'Form':
        """
        Deserializa um dicionário para um objeto.

        Parâmetros
        ----------
        data : dict[str, Any]
            Mapeamento de nomes de atributos para valores.

        Retorna
        -------
        Form
            O objeto deserializado.
        """
        for key, value in data.items():
            if isinstance(value, dict):
                data[key] = Form.from_data(value)
        # Obtém o atributo class_name enquanto
        # o deixa de fora do dicionário de dados
        class_name = data.pop('class_name')
        obj = eval(class_name)(**data)

        return obj

    @abstractmethod
    def submit_action(self) -> None:
        """Ação a ser executada quando o formulário é enviado."""
        pass

    def append_field(self, field: Field) -> None:
        """
        Adiciona um campo ao formulário.

        Parâmetros
        ----------
        field : Field
            O campo a ser adicionado.
        """
        self.fields.append(field)

    def search_action(self) -> dict[str, Any] | None:
        """Action to be performed when the search form is submitted."""
        db_result = self.db_manager.get_by_id(
            self.db_collection, self.id_field.value
        )
        if db_result:
            return db_result
        else:
            st.error("ID não encontrado.")
            return None

    def render_search_field(self) -> dict[str, Any] | None:
        """Renders the search field on the page."""
        result = None
        with st.form(key=self.title + " ID"):
            self.id_field.render()
            if st.form_submit_button(label='Buscar'):
                result = self.search_action()
                if result:
                    st.success('ID encontrado')
                    st.subheader('Informações:')
                    st.write(result)
                else:
                    st.error('ID não encontrado.')
        return result

    def render(self) -> None:
        """Renders the form on the page."""
        st.subheader(self.title)
        st.markdown(self.description)
        if self.id_field:
            field_values = self.render_search_field()
        with st.form(key=self.title):
            for field in self.fields:
                field.render()
            if st.form_submit_button(label='Enviar'):
                self.submit_action()

    def get_form_values(self) -> dict[str, Any]:
        """
        Converte os valores do formulário para um dicionário.

        Retorna
        -------
        dict[str, Any]
            Mapeamento de nomes de atributos para valores.
        """
        form_values = {}
        for field in self.fields:
            # Se o campo for do tipo data, converte o valor para
            # datetime.datetime, para que o banco de dados possa
            # armazenar corretamente
            if field.type == 'date':
                form_values[field.label] = datetime.datetime.combine(
                    field.value,
                    datetime.time.min
                )
            else:
                form_values[field.label] = field.value
        return form_values

    def get_id_field_value(self) -> str:
        """
        Retorna o valor do campo de ID.

        Retorna
        -------
        str
            O valor do campo de ID.

        Raises
        ------
        NoIdError
            Se o formulário não tiver um campo de ID.
        """
        if self.id_field is None:
            raise NoIdError()
        else:
            return self.id_field.value
