from abc import ABC
from datetime import datetime

import pandas as pd
import streamlit as st

from src.database.database import DatabaseManager


class Page(ABC):
    def __init__(
        self,
        title: str,
        description: str,
    ) -> None:
        self.title = title
        self.description = description
        self.elements = []

    def render(self) -> None:
        """Renders the page in the usual organization."""
        st.title(self.title)
        st.write(self.description)


class PaymentControlPage(Page):
    def __init__(self) -> None:
        title = "Controle de Pagamentos"
        description = "Página para controle de pagamentos."
        super().__init__(title, description)
        self.db_manager: DatabaseManager = DatabaseManager.instance()
        self.df = pd.DataFrame(self.db_manager.get_all('payment')).T
        self.index = st.session_state.get('payment_index', 0)

    def _count_payments(self) -> int:
        """Counts the number of payments."""
        return len(self.df)

    def _count_paid_payments(self) -> int:
        """Counts the number of pending payments."""
        return self.df['Pago'].sum()

    def _get_next_pending_payment(self) -> pd.Series:
        """Gets the next pending payment."""
        left_payments = self.df[self.df['Pago'] == False]
        if len(left_payments) == 0:
            return None
        # Se houver pagamentos pendentes, puxa os outros dados do banco
        beneficiaries = pd.DataFrame(self.db_manager.get_all('beneficiary')).T
        beneficiaries = beneficiaries.reset_index(names=['ID do Beneficiário'])
        people = pd.DataFrame(self.db_manager.get_all('person')).T
        people = people.reset_index(names=['ID da Pessoa'])
        left_payments = left_payments.join(
            beneficiaries.set_index('ID do Beneficiário'),
            on='ID do Beneficiário'
        )
        left_payments = left_payments.join(
            people.set_index('ID da Pessoa'),
            on='ID da Pessoa'
        )
        return left_payments.iloc[self.index], self.index

    def _pay_payment(self, payment: pd.Series, payment_idx: str) -> None:
        """Pays the given payment."""
        paid_payment = payment.to_dict()
        paid_payment['Pago'] = True
        # Seleciona apenas as chave-valor pertencentes ao
        # objeto pagamento
        keys = ['Valor',
                'Data do Pagamento',
                'ID do Administrador',
                'ID do Beneficiário',
                'Pago',
                'Data de Referência']
        paid_payment = {k: v for k, v in paid_payment.items()
                        if k in keys}
        # Converte os valores para o tipo correto
        paid_payment['Valor'] = float(paid_payment['Valor'])
        paid_payment['Data do Pagamento'] = datetime.fromtimestamp(
            int(paid_payment['Data do Pagamento'].timestamp())
        )
        paid_payment['Pago'] = bool(paid_payment['Pago'])
        paid_payment['Data de Referência'] = datetime.fromtimestamp(
            int(paid_payment['Data de Referência'].timestamp())
        )
        st.write(paid_payment)
        st.write(payment)
        # Atualiza o pagamento no banco
        self.db_manager.update(
            'payment',
            str(payment_idx),
            {'Pago': True}
        )

    def show_table(self) -> None:
        """Shows the table of the managed elements on the page."""
        st.dataframe(self.df)

    def show_metrics(self) -> None:
        """Shows the metrics of the managed elements on the page."""
        total = self._count_payments()
        paid = self._count_paid_payments()
        pending = total - paid
        # Generate random metrics
        with st.expander("Métricas", expanded=True):
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric(label="Total", value=total)
            with col2:
                st.metric(label="Pago", value=paid)
            with col3:
                st.metric(label="Pendente", value=pending)

    def show_next_payment(self) -> None:
        """Shows the control panel of the managed elements on the page."""
        next_payment, payment_idx = self._get_next_pending_payment()
        if next_payment is None:
            st.write("Todos os pagamentos concluídos! ✅🫡")
        else:
            st.subheader(f"Beneficiário: {next_payment['Nome']}")
            st.header(f"Valor: R${next_payment['Valor']}")
            st.write(f"CPF: {next_payment['CPF']}")
            st.write(f"Email: {next_payment['Email']}")
            with st.expander("Mais Informações", expanded=True):
                st.write(
                    "Descrição do Transporte: "
                    f"{next_payment['Descrição do Transporte']}"
                )
                st.write(
                    "Custo do Transporte: "
                    f"{next_payment['Custo do Transporte']}"
                )
                st.write(
                    "Data de Nascimento: "
                    f"{next_payment['Data de Nascimento']}"
                )
                st.caption(
                    f"ID do Beneficiário: {next_payment['ID do Beneficiário']}"
                )
                st.caption(
                    f"ID da Pessoa: {next_payment['ID da Pessoa']}"
                )
                st.caption(
                    "ID do Administrador Responsável pelo Pagamento: "
                    f"{next_payment['ID do Administrador']}"
                )
                st.caption(
                    f"Data de Referência: {next_payment['Data de Referência']}"
                )
                st.caption(
                    f"Endereço: {next_payment['Endereço']}"
                )
            if st.button("Marcar como Pago"):
                self._pay_payment(next_payment, payment_idx)
                self.index += 1
                st.session_state['payment_index'] = self.index
                st.success("Pagamento marcado como pago! ✅🫡."
                           "Pressione R para atualizar.")
            if st.button("Ir para o Próximo"):
                self.index += 1
                st.session_state['payment_index'] = self.index
                st.info("Passando para o próximo pagamento."
                        "Pressione R para atualizar.")
            if st.button("Recomeçar Pagamentos"):
                st.session_state['payment_index'] = 0
                st.info("Reiniciando os pagamentos."
                        "Pressione R para atualizar.")

    def render(self) -> None:
        super().render()
        self.show_table()
        self.show_metrics()
        self.show_next_payment()
