from .base_forms import (CreationForm, UpdateForm, DeletionForm)
from .fields import SelectBoxField
from src.database.database import DatabaseManager


class AdministratorCreationForm(CreationForm):
    def __init__(self) -> None:
        self.db_manager = DatabaseManager.instance()
        super().__init__(
            title="Formulário de Criação de Administrador",
            description=(
                "Preencha os campos abaixo para criar um novo administrador."
            ),
            fields=[
                SelectBoxField(
                    label="ID do Diretor",
                    options=self.db_manager.get_all_keys("director")
                ),
            ],
            db_collection="administrator"
        )


class AdministratorUpdateForm(UpdateForm):
    def __init__(self) -> None:
        self.db_manager = DatabaseManager.instance()
        super().__init__(
            title="Formulário de Atualização de Administrador",
            description=(
                "Preencha os campos abaixo para atualizar um administrador."
            ),
            id_field=SelectBoxField(
                label="ID do Administrador",
                options=self.db_manager.get_all_keys("administrator")
            ),
            fields=[],
            db_collection="administrator"
        )


class AdministratorDeletionForm(DeletionForm):
    def __init__(self) -> None:
        self.db_manager = DatabaseManager.instance()
        super().__init__(
            title="Formulário de Remoção de Administrador",
            description="Selecione o ID do administrador que deseja remover.",
            id_field=SelectBoxField(
                label="ID do Administrador",
                options=self.db_manager.get_all_keys("administrator")
            ),
            db_collection="administrator"
        )
