import streamlit as st

from src.interface.manager_pages import PresenceListPage

st.set_page_config(
    page_title="Lista de Presença",
    page_icon="📝",
)

page = PresenceListPage()
page.render()
