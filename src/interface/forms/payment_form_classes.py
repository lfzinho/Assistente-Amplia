from datetime import datetime

from .base_forms import (CreationForm, UpdateForm, DeletionForm)
from .fields import DateField, NumberField, SelectBoxField, TextField
from src.database.database import DatabaseManager


class PaymentCreationForm(CreationForm):
    def __init__(self) -> None:
        self.db_manager = DatabaseManager.instance()
        super().__init__(
            title="Formulário de Criação de Pagamento",
            description=(
                "Preencha os campos abaixo para criar um novo pagamento."
            ),
            fields=[
                SelectBoxField(
                    label="ID do Beneficiário",
                    options=self.db_manager.get_all_keys("beneficiary")
                ),
                SelectBoxField(
                    label="ID do Administrador",
                    options=self.db_manager.get_all_keys("administrator")
                ),
                NumberField(label="Valor", value=0.0),
                DateField(label="Data do Pagamento", value=datetime.now()),
                DateField(label="Data de Referência", value=datetime.now()),
            ],
            db_collection='payment'
        )


class PaymentUpdateForm(UpdateForm):
    def __init__(self) -> None:
        self.db_manager = DatabaseManager.instance()
        super().__init__(
            title="Formulário de Atualização de Pagamento",
            description=(
                "Preencha os campos abaixo para atualizar um pagamento."
            ),
            id_field=SelectBoxField(
                label="ID do Pagamento",
                options=self.db_manager.get_all_keys("payment")
            ),
            fields=[
                SelectBoxField(
                    label="ID do Beneficiário",
                    options=self.db_manager.get_all_keys("beneficiary")
                ),
                SelectBoxField(
                    label="ID do Administrador",
                    options=self.db_manager.get_all_keys("administrator")
                ),
                NumberField(label="Valor", value=0.0),
                DateField(label="Data do Pagamento", value=datetime.now()),
                DateField(label="Data de Referência", value=datetime.now()),
            ],
            db_collection='payment'
        )


class PaymentDeletionForm(DeletionForm):
    def __init__(self) -> None:
        self.db_manager = DatabaseManager.instance()
        super().__init__(
            title="Formulário de Remoção de Pagamento",
            description="Selecione o ID do pagamento que deseja remover.",
            id_field=SelectBoxField(
                label="ID do Pagamento",
                options=self.db_manager.get_all_keys("pagamento")
            ),
            db_collection='pagamento'
        )
