import streamlit as st

from src.interface.especific_pages import PaymentControlPage

st.set_page_config(
    page_title="Controle de Pagamentos",
    page_icon="💰",
)

page = PaymentControlPage()
page.render()
