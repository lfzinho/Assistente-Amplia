from datetime import datetime

from .base_forms import (CreationForm, UpdateForm, DeletionForm)
from .fields import (
    CheckboxField,
    DateField,
    NumberField,
    SelectBoxField,
)
from src.database.DAOFactory import DAOFactory


class PaymentCreationForm(CreationForm):
    def __init__(self) -> None:
        super().__init__(
            title="Formulário de Criação de Pagamento",
            description=(
                "Preencha os campos abaixo para criar um novo pagamento."
            ),
            fields=[
                SelectBoxField(
                    label="ID do Beneficiário",
                    options=DAOFactory.get_dao("beneficiary").get_all_keys()
                ),
                SelectBoxField(
                    label="ID do Administrador",
                    options=DAOFactory.get_dao("administrator").get_all_keys()
                ),
                NumberField(label="Valor", value=0.0),
                CheckboxField(label="Pago", value=False),
                DateField(label="Data do Pagamento", value=datetime.now()),
                DateField(label="Data de Referência", value=datetime.now()),
            ],
            db_collection='payment'
        )


class PaymentUpdateForm(UpdateForm):
    def __init__(self) -> None:
        super().__init__(
            title="Formulário de Atualização de Pagamento",
            description=(
                "Preencha os campos abaixo para atualizar um pagamento."
            ),
            id_field=SelectBoxField(
                label="ID do Pagamento",
                options=DAOFactory.get_dao("payment").get_all_keys()
            ),
            fields=[
                SelectBoxField(
                    label="ID do Beneficiário",
                    options=DAOFactory.get_dao("beneficiary").get_all_keys()
                ),
                SelectBoxField(
                    label="ID do Administrador",
                    options=DAOFactory.get_dao("administrator").get_all_keys()
                ),
                NumberField(label="Valor", value=0.0),
                CheckboxField(label="Pago", value=False),
                DateField(label="Data do Pagamento", value=datetime.now()),
                DateField(label="Data de Referência", value=datetime.now()),
            ],
            db_collection='payment'
        )


class PaymentDeletionForm(DeletionForm):
    def __init__(self) -> None:
        super().__init__(
            title="Formulário de Remoção de Pagamento",
            description="Selecione o ID do pagamento que deseja remover.",
            id_field=SelectBoxField(
                label="ID do Pagamento",
                options=DAOFactory.get_dao("payment").get_all_keys()
            ),
            db_collection='payment'
        )
