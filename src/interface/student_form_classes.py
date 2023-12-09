import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

import datetime
from abc import ABC, abstractmethod
import streamlit as st
from src.interface.form_classes import (CreationForm, UpdateForm, DeletionForm)
from src.interface.fields import *
from src.database.database import DatabaseManager


class StudentCreationForm(CreationForm):
    def __init__(self):
        self.db_manager = DatabaseManager.instance()
        super().__init__(
            title="Formulário de Criação de Estudante",
            description="Preencha os campos abaixo para criar um novo estudante.",
            fields=[
                SelectBoxField(
                    label="ID do Beneficiário",
                    options=self.db_manager.get_all_keys("beneficiary")
                ),
                TextField(label="Responsável Financeiro", value=""),
            ],
            db_collection='student'
        )


class StudentUpdateForm(UpdateForm):
    def __init__(self):
        self.db_manager = DatabaseManager.instance()
        super().__init__(
            title="Formulário de Atualização de Estudante",
            description="Preencha os campos abaixo para atualizar um estudante.",
            id_field=SelectBoxField(
                label="ID do Beneficiário",
                options=self.db_manager.get_all_keys("beneficiary")
            ),
            fields=[
                TextField(label="Responsável Financeiro", value=""),
            ],
            db_collection='student'
        )


class StudentDeletionForm(DeletionForm):
    def __init__(self):
        self.db_manager = DatabaseManager.instance()
        super().__init__(
            title="Formulário de Remoção de Estudante",
            description="Selecione o ID do estudante que deseja remover.",
            id_field=SelectBoxField(
                label="ID do Estudante",
                options=self.db_manager.get_all_keys("student")
            ),
            db_collection='student'
        )
