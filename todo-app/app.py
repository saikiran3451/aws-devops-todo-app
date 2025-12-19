from flask import Flask, render_template, request, redirect
import mysql.connector
import subprocess

app = Flask(__name__)

def get_db_password():
    cmd = [
        "aws", "ssm", "get-parameter",
        "--name", "/demo/mysql/password",
        "--with-decryption",
        "--query", "Parameter.Value",
        "--output", "text",
        "--region", "us-east-1"
    ]
    return subprocess.check_output(cmd).decode().strip()

def get_db_connection():
    return mysql.connector.connect(
        host="demo-mysql-db.csjsgq4sko75.us-east-1.rds.amazonaws.com",
        user="admin",
        password=get_db_password(),
        database="demodb"
    )

@app.route("/", methods=["GET", "POST"])
def index():
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == "POST":
        task = request.form["task"]
        cursor.execute("INSERT INTO todos (task) VALUES (%s)", (task,))
        conn.commit()
        return redirect("/")

    cursor.execute("SELECT task FROM todos")
    tasks = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("index.html", tasks=tasks)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

