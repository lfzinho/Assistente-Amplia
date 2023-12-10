from datetime import datetime

from src.database.database import DatabaseManager
from .base_forms import (CreationForm, UpdateForm, DeletionForm)
from .fields import DateField, SelectBoxField


class DirectorCreationForm(CreationForm):
    def __init__(self) -> None:
        self.db_manager = DatabaseManager.instance()
        super().__init__(
            title="Formulário de Criação de Diretor",
            description="Preencha os campos abaixo para criar um novo diretor.",
            fields=[
                SelectBoxField(
                    label="ID do Analista",
                    options=self.db_manager.get_all_keys("analyst")
                ),
                DateField(
                    label="Data de Admissão na Direção",
                    value=datetime.today()
                ),
                DateField(
                    label="Data de Término na Direção",
                    value=None
                ),
            ],
            db_collection="director"
        )


class DirectorUpdateForm(UpdateForm):
    def __init__(self) -> None:
        self.db_manager = DatabaseManager.instance()
        super().__init__(
            title="Formulário de Atualização de Diretor",
            description="Preencha os campos abaixo para atualizar um diretor.",
            id_field=SelectBoxField(
                label="ID do Diretor",
                options=self.db_manager.get_all_keys("director")
            ),
            fields=[
                DateField(
                    label="Data de Admissão na Direção",
                    value=datetime.today()
                ),
                DateField(
                    label="Data de Término na Direção",
                    value=None
                ),
            ],
            db_collection="director"
        )


class DirectorDeletionForm(DeletionForm):
    def __init__(self) -> None:
        self.db_manager = DatabaseManager.instance()
        super().__init__(
            title="Formulário de Remoção de Diretor",
            description="Selecione o ID do diretor que deseja remover.",
            id_field=SelectBoxField(
                label="ID do Diretor",
                options=self.db_manager.get_all_keys("director")
            ),
            db_collection="director"
        )
