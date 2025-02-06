from flask import Flask, jsonify
import pyodbc

app = Flask(__name__)

# Database connection
def get_db_connection():
    # Use your provided connection details
    conn = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=195.201.83.144;'  # Your server address
        'DATABASE=geoAdmin;'      # Your database name
        'UID=geoAdmin;'           # Your username
        'PWD=GeoSoft@123;'        # Your password
    )
    return conn

# API route to fetch data from MasParty table
@app.route('/geosoft/mas_party', methods=['GET'])
def get_mas_party_data():
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
       
        query = "SELECT Pty_Code, Pty_Name, Validity, Active FROM MasParty"
        cursor.execute(query)
        result = cursor.fetchall()

        # Get column names
        columns = [column[0] for column in cursor.description]

        # Convert rows to JSON-friendly format
        data = [dict(zip(columns, row)) for row in result]

        return jsonify(data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)