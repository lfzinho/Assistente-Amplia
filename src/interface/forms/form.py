import datetime
from abc import ABC, abstractmethod
from typing import Any

import streamlit as st

from src.database.database import DatabaseManager
from .fields import Field, SelectBoxField


class Form(ABC):
    def __init__(
        self,
        title: str,
        description: str,
        fields: list[Field],
        id_field: SelectBoxField = None,
        db_collection: str = None
    ) -> None:
        self.title = title
        self.description = description
        self.fields = fields
        self.id_field = id_field
        self.db_collection = db_collection

        self.db_manager = DatabaseManager.instance()

    @abstractmethod
    def submit_action(self) -> None:
        """Action to be performed when the form is submitted."""
        pass

    def append_field(self, field: Field) -> None:
        """Appends a field to the form."""
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

    def get_id_field_value(self) -> str | None:
        """Returns the value of the ID field."""
        # TODO implementar erro customizado
        if self.id_field:
            return self.id_field.value
        else:
            return None
