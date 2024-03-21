import sqlite3
import re
from utils import printTable

def printShowWithTicketsByDate(date):
    con = sqlite3.connect("trondelagTeater.db")
    cursor = con.cursor()
    cursor.execute("""PRAGMA encoding = "UTF-8" """)

    cursor.execute("""
    SELECT 
        F.Dato, 
        F.Klokkeslett, 
        TS.Tittel as TeaterStykkeTittel, 
        COUNT(b.BillettID) as AntallBilletter
    FROM Forestilling F
    JOIN TeaterStykke TS ON F.TeaterStykke = TS.TeaterStykkeID
    LEFT JOIN Billett b ON F.TeaterStykke = b.TeaterStykke AND F.Dato = b.Dato AND F.Klokkeslett = b.Klokkeslett
    WHERE F.Dato = ?
    GROUP BY F.Dato, F.Klokkeslett, TS.Tittel
    """, [date])
    shows_and_tickets = cursor.fetchall()

    printTable(["Dato", "Klokkeslett", "TeaterStykke", "Antall solgte billetter"], shows_and_tickets)
    con.close()

show_date = input("Skriv inn datoen du vil vise billetter til (FORMAT DD-MM-YYYY): ")
try:
    date_pattern = r'^\d{2}-\d{2}-\d{4}$'
        
    if not re.match(date_pattern, show_date):
        raise Exception("Dato er på feil format. Det riktige formatet er 'dd-mm-yyyy'")
        
    printShowWithTicketsByDate(show_date)
except Exception as error:
    print(error)
