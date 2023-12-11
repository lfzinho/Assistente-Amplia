from abc import ABC
from datetime import datetime

import pandas as pd
import streamlit as st

from src.database.database import DatabaseManager
from src.database.DAOFactory import DAOFactory


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
        self.dao = DAOFactory.get_dao('payment')

    def _pay_payment(self, payment: pd.Series, payment_idx: str) -> None:
        st.write(payment)
        paid_payment = self.dao.pay_payment(payment, payment_idx)
        st.write(paid_payment)

    def show_table(self) -> None:
        """Shows the table of the managed elements on the page."""
        st.dataframe(self.dao.df)

    def show_metrics(self) -> None:
        """Shows the metrics of the managed elements on the page."""
        total = self.dao.count_payments()
        paid = self.dao.count_paid_payments()
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
        next_payment, payment_idx = self.dao.get_next_pending_payment()
        if next_payment is None:
            st.write("Todos os pagamentos concluídos! ✅")
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
                st.success("Pagamento marcado como pago! ✅."
                           "Pressione R para atualizar.")

    def render(self) -> None:
        super().render()
        self.show_table()
        self.show_metrics()
        self.show_next_payment()
