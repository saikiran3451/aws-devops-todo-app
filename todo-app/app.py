import boto3
import pymysql
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

def get_db_connection():
    ssm = boto3.client("ssm", region_name="us-east-1")

    host = ssm.get_parameter(Name="/demo/mysql/host")["Parameter"]["Value"]
    user = ssm.get_parameter(Name="/demo/mysql/user")["Parameter"]["Value"]
    password = ssm.get_parameter(
        Name="/demo/mysql/password",
        WithDecryption=True
    )["Parameter"]["Value"]
    name = ssm.get_parameter(Name="/demo/mysql/name")["Parameter"]["Value"]

    return pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=name
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

    cursor.execute("SELECT * FROM todos")
    todos = cursor.fetchall()

    return render_template("index.html", todos=todos)

if __name__ == "__main__":
    app.run()

