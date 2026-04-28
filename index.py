import os
from flask import Flask
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

PORT = int(os.getenv("PORT", 3000))

@app.route("/")
def hello():
    return "Hello World!"


def connect_to_mysql():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST"),
            port=int(os.getenv("MYSQL_PORT", 3306)),
            user=os.getenv("MYSQL_USERNAME"),
            password=os.getenv("MYSQL_ROOT_PASSWORD"),
            database=os.getenv("MYSQL_DATABASE")
        )

        if connection.is_connected():
            print("Connected to MySQL!")

        return connection

    except mysql.connector.Error as err:
        print("The error is:", err)
        return None


if __name__ == "__main__":
    db_connection = connect_to_mysql()

    app.run(host="0.0.0.0", port=PORT)
