import streamlit as st

from src.interface.manager_pages import AdministratorPage

st.set_page_config(
    page_title="Administrador",
    page_icon="👨‍💼"
)

page = AdministratorPage()
page.render()
