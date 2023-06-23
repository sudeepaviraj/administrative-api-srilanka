import json
import mysql.connector
from dotenv.main import load_dotenv
import os
load_dotenv()


def Query(sql):
    connection = mysql.connector.connect(
        host=os.environ["DATABASE_HOST_TEST"],
        port=os.environ["DATABASE_PORT_TEST"],
        user=os.environ["DATABASE_USER_TEST"],
        password=os.environ["DATABASE_PASSWORD_TEST"],
        database=os.environ["DATABASE_NAME_TEST"]
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
        host=os.environ["DATABASE_HOST_TEST"],
        port=os.environ["DATABASE_PORT_TEST"],
        user=os.environ["DATABASE_USER_TEST"],
        password=os.environ["DATABASE_PASSWORD_TEST"],
        database=os.environ["DATABASE_NAME_TEST"]
    )
    dataset = []
    try:
        curser = connection.cursor()
        curser.execute(sql)
        try:
            connection.close()
            return curser.fetchall()
        except Exception as e:
            connection.close()
            return "fetch failed"
    except Exception as e:
        raise SyntaxError(e)
