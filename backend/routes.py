from flask import Blueprint, jsonify
from db_connection import get_db_connection

api = Blueprint('api', __name__)

@api.route('/api/notes', methods=['GET'])
def get_notes():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM materials")  # Sesuaikan dengan tabel kamu
        notes = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(notes)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
