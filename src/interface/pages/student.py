import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))

import streamlit as st
from src.interface.manager_pages import StudentPage

st.set_page_config(
    page_title="Estudante",
    page_icon="📖",
)

page = StudentPage()
page.render()
