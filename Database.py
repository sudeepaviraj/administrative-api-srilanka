import json

import mysql.connector

def Query(sql):
    connection = mysql.connector.connect(
        host="YOUR DATABASE HOST",
        port="YOUR DATABASE PORT",
        user="YOUR DATABASE HOST",
        password="YOUR DATABASE PASSWORD",
        database="YOUR DATABASE"
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
        host="YOUR DATABASE HOST",
        port="YOUR DATABASE PORT",
        user="YOUR DATABASE HOST",
        password="YOUR DATABASE PASSWORD",
        database="YOUR DATABASE"
    )
    dataset = []
    try:
        curser = connection.cursor()
        curser.execute(sql)
        responses = curser.fetchall()
        try:
            for response in responses:
                dataset.append({"id": response[0], "name": response[1].decode("utf-8")})
        except Exception as e:
            for response in responses:
                dataset.append({"id": response[0], "name": response[1]})
        connection.close()
        return dataset
    except Exception as e:
        raise SyntaxError(e)