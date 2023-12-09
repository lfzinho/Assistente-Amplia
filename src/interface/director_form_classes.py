import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

import datetime
from abc import ABC, abstractmethod
import streamlit as st
from src.interface.form_classes import (CreationForm, UpdateForm, DeletionForm)
from src.interface.fields import *


class DirectorCreationForm(CreationForm):
    def __init__(self):
        super().__init__(
            title="Formulário de Criação de Diretor",
            description="Preencha os campos abaixo para criar um novo diretor.",
            fields=[
                SelectBoxField(
                    label="ID do Analista",
                    value="1",
                    options=["1", "2", "3"]
                ),
                DateField(
                    label="Data de Admissão na Direção",
                    value=datetime.datetime.today()
                ),
                DateField(
                    label="Data de Término na Direção",
                    value=None
                ),
            ],
            db_collection="director"
        )


class DirectorUpdateForm(UpdateForm):
    def __init__(self):
        super().__init__(
            title="Formulário de Atualização de Diretor",
            description="Preencha os campos abaixo para atualizar um diretor.",
            id_field=SelectBoxField(
                label="ID do Diretor",
                value="1",
                options=["1", "2", "3"]
            ),
            fields=[
                DateField(
                    label="Data de Admissão na Direção",
                    value=datetime.datetime.today()
                ),
                DateField(
                    label="Data de Término na Direção",
                    value=None
                ),
            ],
            db_collection="director"
        )


class DirectorDeletionForm(DeletionForm):
    def __init__(self):
        super().__init__(
            title="Formulário de Remoção de Diretor",
            description="Selecione o ID do diretor que deseja remover.",
            id_field=SelectBoxField(
                label="ID do Diretor",
                value="1",
                options=["1", "2", "3"]
            ),
            db_collection="director"
        )
