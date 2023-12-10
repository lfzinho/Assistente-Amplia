import streamlit as st
import streamlit_toggle as tog

path = str(os.path.join(os.path.dirname(__file__), '../..'))
from src.authentication.authentication import Authentication

auth_instance = Authentication()

def login_page():
    """Página de login"""
    st.title("Entrar")
    email = st.text_input("E-mail:", key="email_login")
    password = st.text_input("Senha:", type="password", key="password_login")
    if st.button("Entrar"):
        if auth_instance.authenticate(email, password):
            st.success(f"Usuário autenticado com sucesso!")
            st.session_state["uid"] = auth_instance.uid
        else:
            st.error("Falha na autenticação. Verifique o e-mail e a senha.")

def register_page():
    """Página de registro"""
    st.title("Registrar")
    email = st.text_input("E-mail:", key="email_register")
    password = st.text_input("Senha:", type="password", key="password_register")
    password_repeat = st.text_input("Repetir senha:", type="password", key="password_register_repeat")

    if st.button("Registrar"):
        if password != password_repeat:
            st.error("As senhas não coincidem.")
            return
        try:
            uid = auth_instance.create_user(email, password)
            st.success(f"Usuário criado com sucesso!")
            st.session_state["uid"] = uid
        except Exception as e:
            st.error(f"Erro ao criar usuário: {e}")

def main():
    st.title("Bem-vindo ao Assistente-Amplia!")
    login, register = st.tabs(["Entrar", "Registrar"])

    with login:
        login_page()
    with register:
        register_page()

if __name__ == "__main__":
    main()
