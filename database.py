import os
import pymssql
from flask import Flask, jsonify

app = Flask(__name__)

def get_db_connection():
    try:
        conn = pymssql.connect(
            server=os.getenv('DB_SERVER'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        return conn
    except Exception as e:
        print("Database connection failed:", str(e))
        return None

@app.route('/geosoft/mas_party', methods=['GET'])
def get_mas_party_data():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500
    
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT Pty_Code, Pty_Name, Validity, Active FROM MasParty")
        result = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        data = [dict(zip(columns, row)) for row in result]
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use Railway's dynamic port
    app.run(debug=True, host='0.0.0.0', port=port)