from datetime import datetime

from src.database.database import DatabaseManager
from .base_forms import (CreationForm, UpdateForm, DeletionForm)
from .fields import DateField, SelectBoxField, TextField


class PersonCreationForm(CreationForm):
    def __init__(self) -> None:
        super().__init__(
            title="Formulário de Criação de Pessoa",
            description=(
                "Preencha os campos abaixo para criar uma nova pessoa."
            ),
            fields=[
                TextField(label="Nome", value=""),
                TextField(label="Email", value=""),
                DateField(label="Data de Cadastro", value=datetime.now()),
                DateField(label="Data de Saída", value=None),
                DateField(label="Data de Nascimento", value=None),
                TextField(label="CPF", value=""),
                TextField(label="Endereço", value=""),
            ],
            db_collection='person'
        )


class PersonUpdateForm(UpdateForm):
    def __init__(self) -> None:
        self.db_manager = DatabaseManager.instance()
        super().__init__(
            title="Formulário de Atualização de Pessoa",
            description="Preencha os campos abaixo para atualizar uma pessoa.",
            id_field=SelectBoxField(
                label="ID da Pessoa",
                options=self.db_manager.get_all_keys("person")
            ),
            fields=[
                TextField(label="Nome", value=""),
                TextField(label="Email", value=""),
                DateField(label="Data de Cadastro", value=datetime.now()),
                DateField(label="Data de Saída", value=None),
                DateField(label="Data de Nascimento", value=None),
                TextField(label="CPF", value=""),
                TextField(label="Endereço", value=""),
            ],
            db_collection='person'
        )


class PersonDeletionForm(DeletionForm):
    def __init__(self) -> None:
        self.db_manager = DatabaseManager.instance()
        super().__init__(
            title="Formulário de Remoção de Pessoa",
            description="Selecione o ID da pessoa que deseja remover.",
            id_field=SelectBoxField(
                label="ID da Pessoa",
                options=self.db_manager.get_all_keys("person")
            ),
            db_collection='person'
        )
