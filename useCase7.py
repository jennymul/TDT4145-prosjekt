import sqlite3

def useCase7(actorName):
    con = sqlite3.connect("trondelagTeater.db")
    cursor = con.cursor()
    cursor.execute("""SELECT DISTINCT Skuespiller.Navn, TeaterStykke.Tittel
FROM RolleIAkt
JOIN SpillesAv ON SpillesAv.Rolle = RolleIAkt.Rolle
JOIN Skuespiller ON Skuespiller.SkuespillerID = SpillesAv.Skuespiller
JOIN TeaterStykke ON TeaterStykke.TeaterStykkeID = RolleIAkt.TeaterStykke
JOIN (
    SELECT Akt.AktNummer, Akt.TeaterStykke
    FROM Skuespiller
    JOIN SpillesAv ON Skuespiller.SkuespillerID = SpillesAv.Skuespiller
    JOIN RolleIAkt ON RolleIAkt.Rolle = SpillesAv.Rolle
    JOIN Akt ON RolleIAkt.Akt = Akt.AktNummer AND RolleIAkt.TeaterStykke = Akt.TeaterStykke
    WHERE Skuespiller.Navn = ?
) AS SkuespillerInfo ON RolleIAkt.Akt = SkuespillerInfo.AktNummer AND RolleIAkt.TeaterStykke = SkuespillerInfo.TeaterStykke;
                    """,[actorName])

    a = cursor.fetchall()
    for x in a[1:]:
        if(x[1] == "Kongsemnene"):
            print(f'{actorName} spilte sammen med {x[0]} i {x[1]}')
    for x in a[1:]:
        if(x[1] == "Størst av alt er Kjærligheten"):
            print(f'{actorName} spilte sammen med {x[0]} i {x[1]}')

actor = input("Skriv inn skuespillernavn: ")
useCase7(actor)
