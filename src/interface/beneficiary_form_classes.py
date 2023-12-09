import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

import datetime
from abc import ABC, abstractmethod
import streamlit as st
from src.interface.form_classes import (CreationForm, UpdateForm, DeletionForm)
from src.interface.fields import *


class BeneficiaryCreationForm(CreationForm):
    def __init__(self):
        super().__init__(
            title="Formulário de Criação de Beneficiário",
            description="Preencha os campos abaixo para criar um novo beneficiário.",
            fields=[
                SelectBoxField(
                    label="ID da Pessoa",
                    value="1",
                    options=["1", "2", "3"]
                ),
                NumberField(label="Custo do Transporte", value=0.0),
                TextField(label="Descrição do Transporte", value=""),
            ],
            db_collection="beneficiary"
        )


class BeneficiaryUpdateForm(UpdateForm):
    def __init__(self):
        super().__init__(
            title="Formulário de Atualização de Beneficiário",
            description="Preencha os campos abaixo para atualizar um beneficiário.",
            id_field=SelectBoxField(
                label="ID do Beneficiário",
                value="1",
                options=["1", "2", "3"]
            ),
            fields=[
                NumberField(label="Custo do Transporte", value=0.0),
                TextField(label="Descrição do Transporte", value=""),
            ],
            db_collection="beneficiary"
        )


class BeneficiaryDeletionForm(DeletionForm):
    def __init__(self):
        super().__init__(
            title="Formulário de Remoção de beneficiário",
            description="Selecione o ID do beneficiário que deseja remover.",
            id_field=SelectBoxField(
                label="ID do Beneficiário",
                value="1",
                options=["1", "2", "3"]
            ),
            db_collection="beneficiary"
        )
