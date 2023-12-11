import streamlit as st

from .form import Form
from .fields import SelectBoxField
from src.database.DAOFactory import DAOFactory


class CreationForm(Form):
    def __init__(
        self,
        title: str,
        description: str,
        fields: list,
        db_collection: str
    ) -> None:
        super().__init__(title, description, fields, None, db_collection)

    def submit_action(self) -> None:
        """Action to be performed when the form is submitted."""
        form_values = self.get_form_values()
        if self.dao.add(form_values):
            st.success("Adicionado com sucesso.")
        else:
            st.error("Falha ao adicionar.")


class UpdateForm(Form):
    def __init__(
        self,
        title: str,
        description: str,
        id_field: SelectBoxField,
        fields: list,
        db_collection: str
    ) -> None:
        super().__init__(title, description, fields, id_field, db_collection)

    def submit_action(self) -> None:
        """Action to be performed when the form is submitted."""
        form_values = self.get_form_values()
        id_value = self.get_id_field_value()
        if self.dao.update(id_value, form_values):
            st.success("Atualizado com sucesso.")
        else:
            st.error("Falha ao atualizar.")


class DeletionForm(Form):
    def __init__(
        self,
        title: str,
        description: str,
        id_field: SelectBoxField,
        db_collection: str
    ) -> None:
        super().__init__(title, description, [], id_field, db_collection)

    def submit_action(self) -> None:
        """Action to be performed when the form is submitted."""
        id_value = self.get_id_field_value()
        if self.dao.delete(id_value):
            st.success("Deletado com sucesso.")
        else:
            st.error("Falha ao deletar.")
