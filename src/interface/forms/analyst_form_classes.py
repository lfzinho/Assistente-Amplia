from .base_forms import (CreationForm, UpdateForm, DeletionForm)
from .fields import SelectBoxField
from src.database.database import DatabaseManager

AREAS = [
    "Administrativo-Financeiro",
    "Marketing",
    "Pedagógico",
    "Presidência",
    "Recursos Humanos",
]


class AnalystCreationForm(CreationForm):
    def __init__(self) -> None:
        self.db_manager = DatabaseManager.instance()
        super().__init__(
            title="Formulário de Criação de Analista",
            description=(
                "Preencha os campos abaixo para criar um novo analista."
            ),
            fields=[
                SelectBoxField(
                    label="ID da Pessoa",
                    options=self.db_manager.get_all_keys("person")
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
        self.db_manager = DatabaseManager.instance()
        super().__init__(
            title="Formulário de Atualização de Analista",
            description=(
                "Preencha os campos abaixo para atualizar um analista."
            ),
            id_field=SelectBoxField(
                label="ID do Analista",
                options=self.db_manager.get_all_keys("analyst")
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
        self.db_manager = DatabaseManager.instance()
        super().__init__(
            title="Formulário de Remoção de Analista",
            description="Selecione o ID do analista que deseja remover.",
            id_field=SelectBoxField(
                label="ID do Analista",
                options=self.db_manager.get_all_keys("analyst")
            ),
            db_collection="analyst"
        )
