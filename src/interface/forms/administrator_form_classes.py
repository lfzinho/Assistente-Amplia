from .base_forms import (CreationForm, UpdateForm, DeletionForm)
from .fields import SelectBoxField
from src.database.DAOFactory import DAOFactory


class AdministratorCreationForm(CreationForm):
    def __init__(self) -> None:
        super().__init__(
            title="Formulário de Criação de Administrador",
            description=(
                "Preencha os campos abaixo para criar um novo administrador."
            ),
            fields=[
                SelectBoxField(
                    label="ID do Diretor",
                    options=DAOFactory.get_dao("director").get_all_keys()
                ),
            ],
            db_collection="administrator"
        )


class AdministratorUpdateForm(UpdateForm):
    def __init__(self) -> None:
        super().__init__(
            title="Formulário de Atualização de Administrador",
            description=(
                "Preencha os campos abaixo para atualizar um administrador."
            ),
            id_field=SelectBoxField(
                label="ID do Administrador",
                options=DAOFactory.get_dao("administrator").get_all_keys()
            ),
            fields=[],
            db_collection="administrator"
        )


class AdministratorDeletionForm(DeletionForm):
    def __init__(self) -> None:
        super().__init__(
            title="Formulário de Remoção de Administrador",
            description="Selecione o ID do administrador que deseja remover.",
            id_field=SelectBoxField(
                label="ID do Administrador",
                options=DAOFactory.get_dao("administrator").get_all_keys()
            ),
            db_collection="administrator"
        )
