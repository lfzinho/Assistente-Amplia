from src.database.database import DatabaseManager
from .base_forms import (CreationForm, UpdateForm, DeletionForm)
from .fields import CheckboxSeriesField, DateField, SelectBoxField


class PresenceListCreationForm(CreationForm):
    def __init__(self) -> None:
        self.db_manager = DatabaseManager.instance()
        beneficiaries = self.db_manager.get_all("beneficiary")
        ben_names = [f"{ben['Nome']}" for ben in beneficiaries]
        ben_ids = list(beneficiaries.keys())
        super().__init__(
            title="Formulário de Criação de Lista de Presença",
            description=(
                "Preencha os campos abaixo para criar uma nova lista de presença."
            ),
            fields=[
                DateField(label="Data da Aula", value=None),
                CheckboxSeriesField(
                    label="ID dos Beneficiários",
                    options=ben_names,
                    key=ben_ids
                ),
            ],
            db_collection="presence_list"
        )


class BeneficiaryUpdateForm(UpdateForm):
    def __init__(self) -> None:
        self.db_manager = DatabaseManager.instance()
        self.db_manager = DatabaseManager.instance()
        beneficiaries = self.db_manager.get_all("beneficiary")
        ben_names = [f"{ben['Nome']}" for ben in beneficiaries]
        super().__init__(
            title="Formulário de Atualização de Lista de Presença",
            description=(
                "Preencha os campos abaixo para atualizar uma lista de presença."
            ),
            id_field=SelectBoxField(
                label="ID da Lista de Presença",
                options=self.db_manager.get_all_keys("beneficiary")
            ),
            fields=[
                DateField(label="Data da Aula", value=None),
                CheckboxSeriesField(
                    label="ID dos Beneficiários",
                    options=ben_names,
                    key=list(beneficiaries.keys())
                ),
            ],
            db_collection="presence_list"
        )


class BeneficiaryDeletionForm(DeletionForm):
    def __init__(self) -> None:
        self.db_manager = DatabaseManager.instance()
        super().__init__(
            title="Formulário de Remoção de Lista de Presença",
            description="Selecione o ID da lista de presença que deseja remover.",
            id_field=SelectBoxField(
                label="ID da Lista de Presença",
                options=self.db_manager.get_all_keys("presence_list")
            ),
            db_collection="presence_list"
        )
