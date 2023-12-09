import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from abc import ABC, abstractmethod
import streamlit as st
from src.interface.form import Form
from src.interface.fields import SelectBoxField


class CreationForm(Form):
    def __init__(self, title: str, description: str, fields: list):
        super().__init__(title, description, fields)

    def submit_action(self):
        """Action to be performed when the form is submitted."""
        pass  # TODO adiciona os dados no banco de dados


class UpdateForm(Form):
    def __init__(self,
                 title: str,
                 description: str,
                 id_field: SelectBoxField,
                 fields: list,
                 db_search_doc: str
        ):
        super().__init__(title, description, fields, id_field, db_search_doc)

    def submit_action(self):
        """Action to be performed when the form is submitted."""
        pass  # TODO atualiza os dados no banco de dados


class DeletionForm(Form):
    def __init__(self,
                 title: str,
                 description: str,
                 id_field: SelectBoxField,
                 db_search_doc: str
        ):
        super().__init__(title, description, [], id_field, db_search_doc)

    def submit_action(self):
        """Action to be performed when the form is submitted."""
        pass  # TODO remove os dados do banco de dados

