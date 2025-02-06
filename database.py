import os
import pymssql
from flask import Flask, jsonify

app = Flask(__name__)

def get_db_connection():
    conn = pymssql.connect(
        server=os.getenv('DB_SERVER'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
    return conn

@app.route('/geosoft/mas_party', methods=['GET'])
def get_mas_party_data():
    conn = get_db_connection()
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
    app.run(debug=True, host='0.0.0.0', port=10000)