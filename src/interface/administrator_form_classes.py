import streamlit as st

from . import _init_path
from src.interface.form_classes import (CreationForm, UpdateForm, DeletionForm)
from src.interface.fields import *
from src.database.database import DatabaseManager


class administratorCreationForm(CreationForm):
    def __init__(self) -> None:
        self.db_manager = DatabaseManager.instance()
        super().__init__(
            title="Formulário de Criação de Administrador",
            description="Preencha os campos abaixo para criar um novo administrador.",
            fields=[
                SelectBoxField(
                    label="ID do Diretor",
                    options=self.db_manager.get_all_keys("director")
                ),
            ],
            db_collection="administrator"
        )


class administratorUpdateForm(UpdateForm):
    def __init__(self) -> None:
        self.db_manager = DatabaseManager.instance()
        super().__init__(
            title="Formulário de Atualização de Administrador",
            description="Preencha os campos abaixo para atualizar um administrador.",
            id_field=SelectBoxField(
                label="ID do Administrador",
                options=self.db_manager.get_all_keys("administrator")
            ),
            fields=[],
            db_collection="administrator"
        )


class administratorDeletionForm(DeletionForm):
    def __init__(self) -> None:
        self.db_manager = DatabaseManager.instance()
        super().__init__(
            title="Formulário de Remoção de Administrador",
            description="Selecione o ID do administrador que deseja remover.",
            id_field=SelectBoxField(
                label="ID do Administrador",
                options=self.db_manager.get_all_keys("administrator")
            ),
            db_collection="administrator"
        )
