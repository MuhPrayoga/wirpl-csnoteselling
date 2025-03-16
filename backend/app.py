import streamlit as st
import mysql.connector

# Konfigurasi koneksi database
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="noteselling-wirpl"
    )

# Streamlit UI
st.title("CS Note Selling - Backend")
st.write("Data dari Database:")

# Fetch data dari database
conn = get_db_connection()
cursor = conn.cursor(dictionary=True)
cursor.execute("SELECT * FROM materials")
data = cursor.fetchall()

for row in data:
    st.write(f"**{row['title']}** - {row['price']}")

cursor.close()
conn.close()
