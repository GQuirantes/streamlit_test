import asyncio

import streamlit as st

ss = st.session_state


def authenticate(username: str, password: str) -> list[str]:

    logins = st.secrets

    i = 1
    for _, user_data in logins.login.items():
        if (
            username == user_data['USERNAME']
            and password == user_data['PASSWORD']
        ):
            ss.username = user_data['USERNAME']
            ss.user_role = user_data['ROLE']
            return True
        i += 1
    return False


# Login form
def show_authenticator():

    # Initialize session state for authentication
    if 'authenticated' not in ss:
        ss.authenticated = False
    if 'username' not in ss:
        ss.username = None
    if 'password' not in ss:
        ss.password = None

    # Login form
    if not ss.authenticated:
        with st.columns(3)[1]:
            st.title('Login')
            username = st.text_input('Username')
            password = st.text_input('Password', type='password')

            if st.button('Login'):
                authenticated = authenticate(username, password)
                if authenticated:
                    ss.authenticated = True
                    st.success('Login realizado')
                    asyncio.sleep(1)
                    st.rerun()
                else:
                    st.error('O username ou password está incorreto')
        st.stop()