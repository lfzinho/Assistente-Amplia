from . import _init_path
import streamlit as st
from src.interface.form import Form
from src.interface.fields import SelectBoxField
from src.database.database import DatabaseManager

dbm = DatabaseManager.instance()

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
        if dbm.add(self.db_collection, form_values):
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
        if dbm.update(self.db_collection, id_value, form_values):
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
        if dbm.delete(self.db_collection, id_value):
            st.success("Deletado com sucesso.")
        else:
            st.error("Falha ao deletar.")
