from abc import ABC

import pandas as pd
import streamlit as st

from src.database.database import DatabaseManager
import random


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

    def show_table(self) -> None:
        """Shows the table of the managed elements on the page."""
        df = pd.DataFrame(self.db_manager.get_all('payment')).T
        st.table(df)

    def show_metrics(self) -> None:
        """Shows the metrics of the managed elements on the page."""
        # Generate random metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(label="Total", value=random.randint(1, 100))
        with col2:
            st.metric(label="Pago", value=random.randint(1, 100))
        with col3:
            st.metric(label="Pendente", value=random.randint(1, 100))

    def show_control_panel(self) -> None:
        """Shows the control panel of the managed elements on the page."""
        st.title("Pagamentos Pendentes (7/20)")
        st.write("Sérgio Moreira")
        st.write("R$ 100,00")
        st.write("PIX: 123456789")
        col1, col2 = st.columns(2)
        with col1:
            st.button("Marcar como Pago")
        with col2:
            st.button("Passar para o Próximo")

    def render(self) -> None:
        super().render()
        self.show_table()
        self.show_metrics()
        self.show_control_panel()
