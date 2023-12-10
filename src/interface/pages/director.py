import streamlit as st

from pages.manager_pages import DirectorPage

st.set_page_config(
    page_title="Diretor",
    page_icon="🫡"
)

page = DirectorPage()
page.render()
