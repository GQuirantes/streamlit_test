import streamlit as st
from src.authentication import show_authenticator
from src.database import get_connection  # Agora importamos de database.py

def buscar_telefone(ext_id):
    """Busca o número de telefone no banco de dados com base no EXT_ID."""
    try:
        conn = get_connection()
        cur = conn.cursor()
        
        query = "SELECT phone_number FROM users WHERE ext_id = %s;"
        cur.execute(query, (ext_id,))
        result = cur.fetchone()

        cur.close()
        conn.close()

        return result[0] if result else None
    except Exception as e:
        st.error(f"Erro ao buscar dados: {e}")
        return None

# Interface do Streamlit
st.set_page_config(page_title="Buscador de Telefones", page_icon="📞")

show_authenticator()  # Exibe o login

st.title('Buscador de Telefones! 📞')

# Input para EXT_ID
ext_id = st.text_input("Insira o EXT_ID:", placeholder="Digite o EXT_ID aqui...")

# Botão para buscar o número de telefone
if st.button("Buscar Telefone 🔍"):
    if ext_id.strip():  # Evita espaços em branco
        phone_number = buscar_telefone(ext_id)
        if phone_number:
            st.success(f"📲 Número de telefone encontrado: {phone_number}")
        else:
            st.error("❌ Nenhum telefone encontrado para este EXT_ID.")
    else:
        st.warning("⚠️ Por favor, insira um EXT_ID válido.")

# Mensagem de rodapé
st.caption("📌 Aplicação de busca de telefones segura e eficiente.")
