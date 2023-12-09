import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

import datetime
from abc import ABC, abstractmethod
import streamlit as st
from src.interface.form_classes import (CreationForm, UpdateForm, DeletionForm)
from src.interface.fields import *


class TeacherCreationForm(CreationForm):
    def __init__(self):
        super().__init__(
            title="Formulário de Criação de Professor",
            description="Preencha os campos abaixo para criar um novo professor.",
            fields=[
                SelectBoxField(
                    label="ID do Beneficiário",
                    value="1",
                    options=["1", "2", "3"]
                ),
                TextField(label="Matéria", value=""),
            ]
        )


class TeacherUpdateForm(UpdateForm):
    def __init__(self):
        super().__init__(
            title="Formulário de Atualização de Professor",
            description="Preencha os campos abaixo para atualizar um professor.",
            id_field=SelectBoxField(
                label="ID do Beneficiário",
                value="1",
                options=["1", "2", "3"]
            ),
            fields=[
                TextField(label="Matéria", value=""),
            ],
            db_search_doc='teacher'
        )


class TeacherDeletionForm(DeletionForm):
    def __init__(self):
        super().__init__(
            title="Formulário de Remoção de Professor",
            description="Selecione o ID do professor que deseja remover.",
            id_field=SelectBoxField(
                label="ID do Professor",
                value="1",
                options=["1", "2", "3"]
            ),
            db_search_doc='teacher'
        )
