import streamlit as st

from src.interface.manager_pages import BeneficiaryPage

st.set_page_config(
    page_title="Beneficiário",
    page_icon="🧑",
)

page = BeneficiaryPage()
page.render()
