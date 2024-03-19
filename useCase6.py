import sqlite3
import re


def listShowsByTicketSales():
    con = sqlite3.connect("trondelagTeater.db")
    cursor = con.cursor()
    cursor.execute("""PRAGMA encoding = "UTF-8" """)

    query = """
    SELECT
        f.Dato, 
        f.Klokkeslett, 
        ts.Tittel as TeaterStykkeTittel, 
        COUNT(b.BillettID) as AntallBilletter
    FROM Forestilling f
    JOIN TeaterStykke ts ON f.TeaterStykke = ts.TeaterStykkeID
    LEFT JOIN Billett b ON f.TeaterStykke = b.TeaterStykke AND f.Dato = b.Dato AND f.Klokkeslett = b.Klokkeslett
    GROUP BY f.Dato, f.Klokkeslett, ts.Tittel
    ORDER BY AntallBilletter DESC
    """
    cursor.execute(query)

    shows = cursor.fetchall()

    for show in shows:
        print(
            f'Forestilling den {show[0]} for teaterstykke "{show[2]}"',
            f" - {show[3]} solge billetter",
        )


listShowsByTicketSales()
