import json
import mysql.connector
from dotenv.main import load_dotenv
import os
load_dotenv()


def Query(sql):
    connection = mysql.connector.connect(
        host=os.environ["DATABASE_HOST"],
        port=os.environ["DATABASE_PORT"],
        user=os.environ["DATABASE_USER"],
        password=os.environ["DATABASE_PASSWORD"],
        database=os.environ["DATABASE_NAME"]
    )
    cursor = connection.cursor()

    try:
        cursor.execute(sql)
        connection.commit()
        connection.close()
        return "done"
    except Exception as e:
        raise SyntaxError(e)


def SelectQuery(sql) -> list:
    connection = mysql.connector.connect(
        host=os.environ["DATABASE_HOST"],
        port=os.environ["DATABASE_PORT"],
        user=os.environ["DATABASE_USER"],
        password=os.environ["DATABASE_PASSWORD"],
        database=os.environ["DATABASE_NAME"]
    )
    dataset = []
    try:
        curser = connection.cursor()
        curser.execute(sql)
        try:
            data = curser.fetchall()
            connection.close()
            return data
        except Exception as e:
            connection.close()
            return "fetch failed"
    except Exception as e:
        raise SyntaxError(e)
