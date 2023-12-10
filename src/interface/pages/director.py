import streamlit as st

from src.interface.manager_pages import DirectorPage

st.set_page_config(
    page_title="Diretor",
    page_icon="🫡"
)

page = DirectorPage()
page.render()
