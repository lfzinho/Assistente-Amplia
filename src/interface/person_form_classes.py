import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

import datetime
from abc import ABC, abstractmethod
import streamlit as st
from src.interface.form_classes import CreationForm, UpdateForm, DeletionForm
from src.interface.fields import *


class PersonCreationForm(CreationForm):
    def __init__(self):
        super().__init__(
            title="Formulário de Criação de Pessoa",
            description="Preencha os campos abaixo para criar uma nova pessoa.",
            fields=[
                TextField(label="Nome", value=""),
                TextField(label="Email", value=""),
                DateField(label="Data de Cadastro", value=datetime.datetime.now()),
                DateField(label="Data de Saída", value=None),
                DateField(label="Data de Nascimento", value=None),
                TextField(label="CPF", value=""),
                TextField(label="Endereço", value=""),
            ],
            db_collection='person'
        )


class PersonUpdateForm(UpdateForm):
    def __init__(self):
        super().__init__(
            title="Formulário de Atualização de Pessoa",
            description="Preencha os campos abaixo para atualizar uma pessoa.",
            id_field=SelectBoxField(
                label="ID da Pessoa",
                value="1",
                options=["1", "2", "3"]
            ),
            fields=[
                TextField(label="Nome", value=""),
                TextField(label="Email", value=""),
                DateField(label="Data de Cadastro", value=datetime.datetime.now()),
                DateField(label="Data de Saída", value=None),
                DateField(label="Data de Nascimento", value=None),
                TextField(label="CPF", value=""),
                TextField(label="Endereço", value=""),
            ],
            db_collection='person'
        )


class PersonDeletionForm(DeletionForm):
    def __init__(self):
        super().__init__(
            title="Formulário de Remoção de Pessoa",
            description="Selecione o ID da pessoa que deseja remover.",
            id_field=SelectBoxField(
                label="ID da Pessoa",
                value="1",
                options=["1", "2", "3"]
            ),
            db_collection='person'
        )
