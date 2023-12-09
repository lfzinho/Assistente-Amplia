from . import _init_path
from src.interface.form_classes import (CreationForm, UpdateForm, DeletionForm)
from src.interface.fields import *

AREAS = [
    "Administrativo-Financeiro",
    "Marketing",
    "Pedagógico",
    "Presidência",
    "Recursos Humanos",
]


class AnalystCreationForm(CreationForm):
    def __init__(self) -> None:
        super().__init__(
            title="Formulário de Criação de Analista",
            description="Preencha os campos abaixo para criar um novo analista.",
            fields=[
                SelectBoxField(
                    label="ID da Pessoa",
                    value="1",
                    options=["1", "2", "3"]
                ),
                SelectBoxField(
                    label="Área do Analista",
                    value=AREAS[0],
                    options=AREAS
                ),
            ],
            db_collection="analyst"
        )


class AnalystUpdateForm(UpdateForm):
    def __init__(self) -> None:
        super().__init__(
            title="Formulário de Atualização de Analista",
            description="Preencha os campos abaixo para atualizar um analista.",
            id_field=SelectBoxField(
                label="ID do Analista",
                value="1",
                options=["1", "2", "3"]
            ),
            fields=[
                SelectBoxField(
                    label="Área do Analista",
                    value=AREAS[0],
                    options=AREAS
                ),
            ],
            db_collection="analyst"
        )


class AnalystDeletionForm(DeletionForm):
    def __init__(self) -> None:
        super().__init__(
            title="Formulário de Remoção de Analista",
            description="Selecione o ID do analista que deseja remover.",
            id_field=SelectBoxField(
                label="ID do Analista",
                value="1",
                options=["1", "2", "3"]
            ),
            db_collection="analyst"
        )
