from .base_forms import (CreationForm, UpdateForm, DeletionForm)
from .fields import SelectBoxField, TextField
from src.database.DAOFactory import DAOFactory


class TeacherCreationForm(CreationForm):
    def __init__(self) -> None:
        super().__init__(
            title="Formulário de Criação de Professor",
            description="Preencha os campos abaixo para criar um novo professor.",
            fields=[
                SelectBoxField(
                    label="ID do Beneficiário",
                    options=DAOFactory.get_dao("beneficiary").get_all()
                ),
                TextField(label="Matéria", value=""),
            ],
            db_collection='teacher'
        )


class TeacherUpdateForm(UpdateForm):
    def __init__(self) -> None:
        super().__init__(
            title="Formulário de Atualização de Professor",
            description=(
                "Preencha os campos abaixo para atualizar um professor."
            ),
            id_field=SelectBoxField(
                label="ID do Beneficiário",
                options=DAOFactory.get_dao("beneficiary").get_all()
            ),
            fields=[
                TextField(label="Matéria", value=""),
            ],
            db_collection='teacher'
        )


class TeacherDeletionForm(DeletionForm):
    def __init__(self) -> None:
        super().__init__(
            title="Formulário de Remoção de Professor",
            description="Selecione o ID do professor que deseja remover.",
            id_field=SelectBoxField(
                label="ID do Professor",
                options=DAOFactory.get_dao("teacher").get_all()
            ),
            db_collection='teacher'
        )
