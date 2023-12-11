import sys
import os
from abc import ABC, abstractmethod
import datetime
from datetime import date
from typing import Any

import firebase_admin
import pandas as pd
from firebase_admin import credentials, firestore

# Administrator, Analyst, BankAccount, Beneficiary, Cash, Director,
# Payment, Pix, Student, Teacher

from src.database.DataAccessObject import DataAccessObject
from src.database.DAOFactory import DAOFactory
from src.database.database import DatabaseManager
from src.models.Analyst import Analyst
from src.models.Administrator import Administrator
from src.models.BankAccount import BankAccount
from src.models.Beneficiary import Beneficiary
from src.models.Cash import Cash
from src.models.Director import Director
from src.models.Payment import Payment
from src.models.Pix import Pix
from src.models.Student import Student
from src.models.Teacher import Teacher


sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))


class PaymentDAO(DataAccessObject):

    def __init__(self):
        super().__init__('payment')
        self.df = pd.DataFrame(self.get_all_data()).T

    def count_payments(self):
        """
        Retorna o número de pagamentos.

        Retorna
        -------
        int
            Número de pagamentos.
        """
        return len(self.df)

    def count_paid_payments(self):
        """
        Retorna o número de pagamentos pagos.

        Retorna
        -------
        int
            Número de pagamentos pagos.
        """
        return self.df['Pago'].sum()

    def get_next_pending_payment(self):
        # Lê os beneficiários e pessoas
        left_payments = self.df[self.df['Pago'] == False]
        if len(left_payments) == 0:
            return None, None
        beneficiaries = pd.DataFrame(
            DAOFactory.get_dao('beneficiary').get_all_data(),
        )
        beneficiaries = beneficiaries.reset_index(
            names=['ID do Beneficiário']
        )
        people = pd.DataFrame(
            DAOFactory.get_dao('person').get_all_data(),
        )
        print(people)
        people = people.reset_index(names=['ID da Pessoa'])
        # Join
        left_payments = left_payments.join(
            beneficiaries.set_index('ID do Beneficiário'),
            on='ID do Beneficiário'
        )
        left_payments = left_payments.join(
            people.set_index('ID da Pessoa'),
            on='ID da Pessoa'
        )

        return left_payments.iloc[0], left_payments.index[0]

    def pay_payment(
        self,
        payment: pd.Series,
        payment_idx: str,
    ) -> None:
        """
        Paga um pagamento.

        Parâmetros
        ----------
        payment : pd.Series
            O pagamento a ser pago.
        payment_idx : str
            O índice do pagamento a ser pago.
        """
        paid_payment = payment.to_dict()
        paid_payment['Pago'] = True
        # Seleciona apenas as chave-valor pertencentes ao
        # objeto pagamento
        keys = [
            'Valor',
            'Data do Pagamento',
            'ID do Administrador',
            'ID do Beneficiário',
            'Pago',
            'Data de Referência'
        ]
        paid_payment = {
            k: v for k, v in paid_payment.items() if k in keys
        }
        # Converte os valores para o tipo correto
        paid_payment['Valor'] = float(paid_payment['Valor'])
        paid_payment['Data do Pagamento'] = datetime.fromtimestamp(
            int(paid_payment['Data do Pagamento'].timestamp())
        )
        paid_payment['Pago'] = bool(paid_payment['Pago'])
        paid_payment['Data de Referência'] = datetime.fromtimestamp(
            int(paid_payment['Data de Referência'].timestamp())
        )
        # Instancia o objeto pagamento
        paid_payment_obj = Payment(
            payment_idx,
            paid_payment['Valor'],
            paid_payment['Data do Pagamento'],
            paid_payment['Data de Referência'],
            paid_payment['ID do Administrador'],
            paid_payment['ID do Beneficiário'],
            paid_payment['Pago'],
        )
        # Atualiza o pagamento no objeto
        payment.paid = True
        # Atualiza o pagamento no banco
        self.update(str(payment_idx), {'Pago': True})

        return paid_payment
