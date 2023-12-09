import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from abc import ABC, abstractmethod
import streamlit as st

from src.interface.fields import Field, SelectBoxField


class Form(ABC):
    def __init__(
            self,
            title: str,
            description: str,
            fields: list[Field],
            id_field: SelectBoxField = None,
            db_search_doc: str = None
        ):
        self.title: str = title
        self.description: str = description
        self.fields: list[Field] = fields
        self.id_field: SelectBoxField = id_field
        self.db_search_doc: str = db_search_doc

    @abstractmethod
    def submit_action(self):
        """Action to be performed when the form is submitted."""
        pass

    def append_field(self, field: Field):
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

    def render(self):
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
