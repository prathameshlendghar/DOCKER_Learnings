from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

# Database connection settings
DB_HOST = "host.docker.internal"
# DB_HOST = "localhost"
DB_NAME = "crud_app_db"
DB_USER = "prathamesh"
DB_PASS = "Pratham"
DB_PORT = "5432"  # Default PostgreSQL port

def connect_db():
    """Function to connect to the PostgreSQL database."""
    try:
        connection = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            port=DB_PORT
        )
        return connection
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

@app.route('/view-records/', methods=['GET'])
def view_records():
    """View all records from a specific table in JSON format."""
    connection = connect_db()
    if connection is None:
        return jsonify({"error": "Database connection failed"}), 500

    try:
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {'employee_records_management_employee'}")
        records = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        
        # Convert records to list of dictionaries
        result = [dict(zip(columns, record)) for record in records]

        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    # Set the environment variable for Flask app
    os.environ["FLASK_APP"] = "app"
    
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000, debug=True)
