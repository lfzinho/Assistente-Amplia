from .base_forms import (CreationForm, UpdateForm, DeletionForm)
from .fields import SelectBoxField, TextField
from src.database.DAOFactory import DAOFactory


class StudentCreationForm(CreationForm):
    def __init__(self) -> None:
        super().__init__(
            title="Formulário de Criação de Estudante",
            description=(
                "Preencha os campos abaixo para criar um novo estudante."
            ),
            fields=[
                SelectBoxField(
                    label="ID do Beneficiário",
                    options=DAOFactory.get_dao("beneficiary").get_all()
                ),
                TextField(label="Responsável Financeiro", value=""),
            ],
            db_collection='student'
        )


class StudentUpdateForm(UpdateForm):
    def __init__(self) -> None:
        super().__init__(
            title="Formulário de Atualização de Estudante",
            description=(
                "Preencha os campos abaixo para atualizar um estudante."
            ),
            id_field=SelectBoxField(
                label="ID do Beneficiário",
                options=DAOFactory.get_dao("beneficiary").get_all()
            ),
            fields=[
                TextField(label="Responsável Financeiro", value=""),
            ],
            db_collection='student'
        )


class StudentDeletionForm(DeletionForm):
    def __init__(self) -> None:
        super().__init__(
            title="Formulário de Remoção de Estudante",
            description="Selecione o ID do estudante que deseja remover.",
            id_field=SelectBoxField(
                label="ID do Estudante",
                options=DAOFactory.get_dao("student").get_all()
            ),
            db_collection='student'
        )
