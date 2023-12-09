import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

import datetime
from abc import ABC, abstractmethod
import streamlit as st
from src.interface.form_classes import (CreationForm, UpdateForm, DeletionForm)
from src.interface.fields import *


class AdmnistratorCreationForm(CreationForm):
    def __init__(self):
        super().__init__(
            title="Formulário de Criação de Administrador",
            description="Preencha os campos abaixo para criar um novo administrador.",
            fields=[
                SelectBoxField(
                    label="ID do Diretor",
                    value="1",
                    options=["1", "2", "3"]
                ),
            ],
            db_collection="admnistrator"
        )


class AdmnistratorUpdateForm(UpdateForm):
    def __init__(self):
        super().__init__(
            title="Formulário de Atualização de Administrador",
            description="Preencha os campos abaixo para atualizar um administrador.",
            id_field=SelectBoxField(
                label="ID do Administrador",
                value="1",
                options=["1", "2", "3"]
            ),
            fields=[],
            db_collection="admnistrator"
        )


class AdmnistratorDeletionForm(DeletionForm):
    def __init__(self):
        super().__init__(
            title="Formulário de Remoção de Administrador",
            description="Selecione o ID do administrador que deseja remover.",
            id_field=SelectBoxField(
                label="ID do Administrador",
                value="1",
                options=["1", "2", "3"]
            ),
            db_collection="admnistrator"
        )
