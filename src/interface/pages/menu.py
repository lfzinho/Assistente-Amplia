import streamlit as st

from src.interface.especific_pages import MenuPage

st.set_page_config(
    page_title="Menu",
    page_icon="Ⓜ️",
)

page = MenuPage()
page.render()
