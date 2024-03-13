import sqlite3

def getShowWithTicketsByDate(date):
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
    WHERE f.Dato = ?
    GROUP BY f.Dato, f.Klokkeslett, ts.Tittel
    """
    cursor.execute(query, [date])

    shows = cursor.fetchall()

    for show in shows:
        print(f'Forestilling den {show[0]} klokken {show[1]} for stykke "{show[2]}"', f' - {show[3]} Billetter')
        
getShowWithTicketsByDate("2003-12-01")
