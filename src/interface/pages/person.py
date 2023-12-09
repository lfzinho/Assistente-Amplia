import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))

import streamlit as st
from src.interface.manager_pages import PersonPage

st.set_page_config(
    page_title="Pessoa",
    page_icon="🧍",
)

page = PersonPage()
page.render()
