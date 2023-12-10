import streamlit as st

from pages.manager_pages import TeacherPage

st.set_page_config(
    page_title="Professor",
    page_icon="👨‍🏫",
)

page = TeacherPage()
page.render()
