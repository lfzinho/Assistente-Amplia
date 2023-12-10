import streamlit as st

from src.interface.manager_pages import PaymentPage

st.set_page_config(
    page_title="Pagamento",
    page_icon="🪙",
)

page = PaymentPage()
page.render()
