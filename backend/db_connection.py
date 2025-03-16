import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="noteselling-wirpl"
    )

def fetch_notes():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM materials")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data

