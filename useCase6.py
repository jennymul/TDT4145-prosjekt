import sqlite3
import re
from utils import printTable

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
    printTable(["Dato", "Klokkeslett", "TeaterStykke", "Antall solgte billetter"], shows)

listShowsByTicketSales()
