import datetime
from abc import ABC, abstractmethod
from typing import Any

import streamlit as st

from . import _init_path
from src.interface.fields import Field, SelectBoxField
from src.database.database import DatabaseManager
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
        id_field: SelectBoxField = None,
        db_collection: str = None
    ) -> None:
        self.title: str = title
        self.description: str = description
        self.fields: list[Field] = fields
        self.id_field: SelectBoxField = id_field
        self.db_collection: str = db_collection

        self.db_manager: DatabaseManager = DatabaseManager.instance()

    @staticmethod
    def is_valid_type(value):
        """Checa se o valor é válido para o firebase"""
        if value is None:
            return True
        return isinstance(value, (list, str, int, float, bool,
            datetime.date, dict, ))

    @staticmethod
    def to_data(obj):
        data = dict()
        for key, value in obj.__dict__.items():
            # removes leading underscore
            key = key.lstrip('_')
            # if value is date
            if isinstance(value, datetime.date):
                data[key] = value.strftime('%Y-%m-%d')
            elif Form.is_valid_type(value):
                data[key] = value
            else:
                data[key] = Form.to_data(value)

        return data

    @staticmethod
    def from_data(data):
        for key, value in data.items():
            if isinstance(value, dict):
                data[key] = Form.from_data(value)
        # gets the class_ attribute while leaving it out of the data
        # dict
        class_ = data.pop('class_')
        obj = eval(f"{class_}(**data)")

        return obj

    @abstractmethod
    def submit_action(self) -> None:
        """Action to be performed when the form is submitted."""
        pass

    def append_field(self, field: Field) -> None:
        """Appends a field to the form."""
        self.fields.append(field)

    def search_action(self):
        """Action to be performed when the search form is submitted."""
        db_result = self.db_manager.get_by_id(self.db_collection, self.id_field.value)
        if db_result:
            return db_result
        else:
            st.error("ID não encontrado.")
            return None

    def render_search_field(self):
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
        """Returns the values of the form in a dictionary."""
        form_values = {}
        for field in self.fields:
            # Se o campo for do tipo data, converte o valor para
            # datetime.datetime, para que o banco de dados possa
            # armazenar corretamente
            if field.type == 'date':
                form_values[field.label] = datetime.datetime.combine(
                    field.value,
                    datetime.datetime.min.time()
                )
            else:
                form_values[field.label] = field.value
        return form_values

    def get_id_field_value(self) -> None:
        """Returns the value of the ID field."""
        # TODO implementar erro customizado
        if self.id_field:
            return self.id_field.value
        else:
            return None
