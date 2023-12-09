import datetime
from abc import ABC, abstractmethod
from typing import Any

import streamlit as st

from . import _init_path
from src.interface.fields import Field, SelectBoxField


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

    @abstractmethod
    def submit_action(self) -> None:
        """Action to be performed when the form is submitted."""
        pass

    def append_field(self, field: Field) -> None:
        """Appends a field to the form."""
        self.fields.append(field)

    def search_action(self):
        """Action to be performed when the search form is submitted."""
        # TODO implementar a busca no banco de dados
        return None

    def render_search_field(self):
        """Renders the search field on the page."""
        result = None
        with st.form(key=self.title + " ID"):
            self.id_field.render()
            if st.form_submit_button(label='Buscar'):
                result = self.id_field.search_action()
                if not result:
                    st.error("ID não encontrado.")
        return result

    def render(self) -> None:
        """Renders the form on the page."""
        st.title(self.title)
        st.markdown(self.description)
        # Se o formulário tiver um campo de ID, cria o formulário de busca
        field_values: list = None
        if self.id_field:
            field_values = self.render_search_field()
        with st.form(key=self.title):
            # Se o formulário tiver um campo de ID, preenche os campos com os
            # valores do banco de dados
            if field_values:
                for field, field_value in zip(self.fields, field_values):
                    field.value = field_value
                    field.render()
            # Se o formulário não tiver um campo de ID, renderiza os campos
            # normalmente
            else:
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
