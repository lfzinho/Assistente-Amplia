import datetime
from abc import ABC, abstractmethod
from typing import Any

import streamlit as st

from .fields import Field, SelectBoxField
from src.database.DAOFactory import DAOFactory
from src.exceptions.interface import NoIdError

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

        self.dao = DAOFactory.get_dao(db_collection)

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
        db_result = self.dao.get_by_id(self.id_field.value)
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
            if field.type == 'date' and field.value is not None:
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
            raise NoIdError('O formulário não possui um campo de ID.')
        else:
            return self.id_field.value
