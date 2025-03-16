import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Sesuaikan dengan konfigurasi MySQL Anda
        password="",
        database="noteselling-wirpl"
    )
