import streamlit as st

from pages.manager_pages import StudentPage

st.set_page_config(
    page_title="Estudante",
    page_icon="📖",
)

page = StudentPage()
page.render()
