from src.database.database import DatabaseManager
from .base_forms import (CreationForm, UpdateForm, DeletionForm)
from .fields import NumberField, SelectBoxField, TextField


class BeneficiaryCreationForm(CreationForm):
    def __init__(self) -> None:
        self.db_manager = DatabaseManager.instance()
        super().__init__(
            title="Formulário de Criação de Beneficiário",
            description=(
                "Preencha os campos abaixo para criar um novo beneficiário."
            ),
            fields=[
                SelectBoxField(
                    label="ID da Pessoa",
                    options=self.db_manager.get_all_keys("person")
                ),
                NumberField(label="Custo do Transporte", value=0.0),
                TextField(label="Descrição do Transporte", value=""),
            ],
            db_collection="beneficiary"
        )


class BeneficiaryUpdateForm(UpdateForm):
    def __init__(self) -> None:
        self.db_manager = DatabaseManager.instance()
        super().__init__(
            title="Formulário de Atualização de Beneficiário",
            description=(
                "Preencha os campos abaixo para atualizar um beneficiário."
            ),
            id_field=SelectBoxField(
                label="ID do Beneficiário",
                options=self.db_manager.get_all_keys("beneficiary")
            ),
            fields=[
                NumberField(label="Custo do Transporte", value=0.0),
                TextField(label="Descrição do Transporte", value=""),
            ],
            db_collection="beneficiary"
        )


class BeneficiaryDeletionForm(DeletionForm):
    def __init__(self) -> None:
        self.db_manager = DatabaseManager.instance()
        super().__init__(
            title="Formulário de Remoção de beneficiário",
            description="Selecione o ID do beneficiário que deseja remover.",
            id_field=SelectBoxField(
                label="ID do Beneficiário",
                options=self.db_manager.get_all_keys("beneficiary")
            ),
            db_collection="beneficiary"
        )
