import streamlit as st

from src.interface.manager_pages import TeacherPage

st.set_page_config(
    page_title="Professor",
    page_icon="👨‍🏫",
)

page = TeacherPage()
page.render()
