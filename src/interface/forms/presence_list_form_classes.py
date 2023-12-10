import pandas as pd

from src.database.database import DatabaseManager
from .base_forms import (CreationForm, UpdateForm, DeletionForm)
from .fields import CheckboxSeriesField, DateField, SelectBoxField


class PresenceListCreationForm(CreationForm):
    def __init__(self) -> None:
        self.db_manager = DatabaseManager.instance()
        beneficiaries = self.db_manager.get_all("beneficiary")
        df_ben = pd.DataFrame(beneficiaries).T
        people = self.db_manager.get_all("person")
        df_people = pd.DataFrame(people).T
        df_people = df_people.reset_index(names=["ID da Pessoa"])
        df = pd.merge(df_ben, df_people, on="ID da Pessoa")
        ben_names = list(df["Nome"])
        ben_ids = list(beneficiaries.keys())
        super().__init__(
            title="Formulário de Criação de Lista de Presença",
            description=(
                "Preencha os campos abaixo para criar uma nova lista de presença."
            ),
            fields=[
                DateField(label="Data da Aula", value=None),
                CheckboxSeriesField(
                    label="ID dos Beneficiários Presentes",
                    options=ben_names,
                    keys=ben_ids,
                    main_key="create"
                ),
            ],
            db_collection="presence_list"
        )


class PresenceListUpdateForm(UpdateForm):
    def __init__(self) -> None:
        self.db_manager = DatabaseManager.instance()
        beneficiaries = self.db_manager.get_all("beneficiary")
        df_ben = pd.DataFrame(beneficiaries).T
        people = self.db_manager.get_all("person")
        df_people = pd.DataFrame(people).T
        df_people = df_people.reset_index(names=["ID da Pessoa"])
        df = pd.merge(df_ben, df_people, on="ID da Pessoa")
        ben_names = list(df["Nome"])
        ben_ids = list(beneficiaries.keys())
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
                    label="ID dos Beneficiários Presentes",
                    options=ben_names,
                    keys=ben_ids,
                    main_key="update"
                ),
            ],
            db_collection="presence_list"
        )


class PresenceListDeletionForm(DeletionForm):
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
