import streamlit as st
import pandas as pd
import mysql.connector

# Koneksi database
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="csnoteselling"
    )

# API untuk mengambil data
st.header("API Backend Streamlit")
if st.button("Tampilkan Data"):
    conn = get_db_connection()
    df = pd.read_sql("SELECT * FROM catatan", conn)
    st.write(df)

