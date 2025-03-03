import streamlit as st
import asyncio

# Gerenciar o estado da sessão
ss = st.session_state

def authenticate(username: str, password: str) -> bool:
    """Verifica se o usuário e a senha estão corretos com base nos segredos armazenados."""
    logins = st.secrets

    for _, user_data in logins.login.items():
        if username == user_data['USERNAME'] and password == user_data['PASSWORD']:
            ss.username = user_data['USERNAME']
            ss.user_role = user_data['ROLE']
            ss.authenticated = True  # Define o estado autenticado como True
            return True

    return False

def show_authenticator():
    """Exibe o formulário de login e autentica o usuário."""
    # Inicializa o estado da sessão para autenticação
    if 'authenticated' not in ss:
        ss.authenticated = False
    if 'username' not in ss:
        ss.username = None
    if 'password' not in ss:
        ss.password = None

    # Se o usuário ainda não está autenticado, exibe o formulário de login
    if not ss.authenticated:
        col1, col2, col3 = st.columns([1, 2, 1])  # Centraliza a UI (coluna do meio é maior)
        with col2:  # Usar apenas a segunda coluna para centralizar o login
            st.title('Login')
            username = st.text_input('Username')
            password = st.text_input('Password', type='password')

            if st.button('Login'):
                if authenticate(username, password):
                    st.success('Login realizado com sucesso!')
                    asyncio.sleep(1)  # Aguarda 1 segundo antes de recarregar a página
                    st.rerun()  # Recarrega a aplicação para atualizar o estado
                else:
                    st.error('O username ou password está incorreto')

    st.stop()  # Impede que o código continue sendo executado caso o usuário não esteja autenticado