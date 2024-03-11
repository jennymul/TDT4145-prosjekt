import sqlite3

def createDatabase():
    con = sqlite3.connect("trondelagTeater.db")
    cursor = con.cursor()
    cursor.execute("""PRAGMA encoding = "UTF-8" """)

    cursor.execute('''CREATE TABLE 
                   ''')