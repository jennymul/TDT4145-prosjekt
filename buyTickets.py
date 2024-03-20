import sqlite3

def buyTickets():
    playID = 2
    hall = 2
    date ='03-02-2024'
    time = '18:30:00'
    prisType = 'Ordinær'
    kundeID = 1

    con = sqlite3.connect("trondelagTeater.db")
    cursor = con.cursor()

    cursor.execute("""
    SELECT P.RadNummer, P.StolNummer, P.Omraade
    FROM Plass AS P
    WHERE P.Sal = 2
      AND NOT EXISTS (
        SELECT 1 
        FROM Billett AS B 
        WHERE B.Stolnummer = P.StolNummer 
          AND B.RadNummer = P.RadNummer 
          AND B.Omraade = P.Omraade 
          AND B.Sal = P.Sal
          AND B.TeaterStykke = 'TeaterStykkeID'
          AND B.Dato = '03-02-2024'
          AND B.Klokkeslett = '18:30:00'
      ) ORDER BY P.RadNummer, P.Omraade;
    """)
    seats = cursor.fetchall()

    s = []
    for i in range(len(seats)):
        row = seats[i][0]
        s = [seats[i]]
        for j in range(8):
            if seats[j][0] == row:
                s.append(seats[j])
            else:
                break
        if len(s) == 9:
            break

    cursor.execute("SELECT Pris FROM PrisType WHERE Type = ? LIMIT 1;", (prisType,))
    ticketPrice = cursor.fetchone()[0]
    totalPrice = ticketPrice * 9

    cursor.execute("""
    SELECT MAX(KjopID) FROM BillettKjop;
    """)
    buyID = cursor.fetchone()
    buyID = 0 if buyID == None else buyID[0] + 1

    cursor.execute("""
    INSERT INTO BillettKjop VALUES (?, ?, ?, ?, ?);
    """, (buyID, totalPrice, date, time, kundeID))

    cursor.execute("""
    SELECT MAX(BillettID) FROM Billett;
    """)
    ticketID = cursor.fetchone()
    ticketID = 0 if ticketID == None else ticketID[0] + 1

    for seat in s:
        cursor.execute("""
        INSERT INTO Billett VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """, (ticketID, prisType, seat[1], seat[0], seat[2], date, time, hall, playID, buyID))
        ticketID += 1
    con.commit()
    con.close()


buyTickets()
