import streamlit as st

from pages.manager_pages import AnalystPage

st.set_page_config(
    page_title="Analista",
    page_icon="📊",
)

page = AnalystPage()
page.render()
