import sys
from pathlib import Path

import streamlit as st

# Adiciona src/ ao path
sys.path.append(str(Path(__file__).parent.parent))

st.set_page_config(
    page_title="Assistente Amplia",
    page_icon="📝",
)

st.title("Assistente de Pagamentos Amplia")
st.subheader("O que deseja fazer?")

btn_container = st.container()
ctt_container = st.container()

if btn_container.button("Gerenciar Pagamentos"):
    ctt_container.write("Tabela de Pagamentos")
if btn_container.button("Gerenciar Beneficiários"):
    ctt_container.write("Tabela de Beneficiários")
if btn_container.button("Gerenciar Membros"):
    ctt_container.write("Tabela de Membros")
