from datetime import datetime

from .base_forms import (CreationForm, UpdateForm, DeletionForm)
from .fields import DateField, SelectBoxField
from src.database.DAOFactory import DAOFactory


class DirectorCreationForm(CreationForm):
    def __init__(self) -> None:
        super().__init__(
            title="Formulário de Criação de Diretor",
            description="Preencha os campos abaixo para criar um novo diretor.",
            fields=[
                SelectBoxField(
                    label="ID do Analista",
                    options=DAOFactory.get_dao("analyst").get_all_keys()
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
        super().__init__(
            title="Formulário de Atualização de Diretor",
            description="Preencha os campos abaixo para atualizar um diretor.",
            id_field=SelectBoxField(
                label="ID do Diretor",
                options=DAOFactory.get_dao("director").get_all_keys()
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
        super().__init__(
            title="Formulário de Remoção de Diretor",
            description="Selecione o ID do diretor que deseja remover.",
            id_field=SelectBoxField(
                label="ID do Diretor",
                options=DAOFactory.get_dao("director").get_all_keys()
            ),
            db_collection="director"
        )
