import streamlit as st
import psycopg2

def get_connection():
    """Cria uma conexão segura com o banco de dados usando credenciais do secrets.toml"""
    db_params = st.secrets["database"]  # Busca as credenciais no secrets.toml
    
    conn = psycopg2.connect(
        user=db_params["user"],
        password=db_params["password"],
        host=db_params["host"],
        port=db_params["port"],
        database=db_params["database"]
    )
    return conn
