import os
import sqlite3


def createDatabase():
    con = sqlite3.connect("trondelagTeater.db")
    cursor = con.cursor()
    cursor.execute("""PRAGMA encoding = "UTF-8" """)

    with open("Database.sql", "r") as file:
        sql_script = file.read()

    sql_commands = sql_script.split(";")

    for command in sql_commands:
        cursor.execute(command)

    con.commit()


createDatabase()
