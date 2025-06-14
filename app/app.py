from flask import Flask, request
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ['DB_HOST'],
        database=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD']
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT message FROM greetings LIMIT 1;')
    message = cur.fetchone()[0]
    cur.close()
    conn.close()
    return f"<h1>{message}</h1>"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

