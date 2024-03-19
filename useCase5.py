import sqlite3


def useCase5():
    con = sqlite3.connect("trondelagTeater.db")
    cursor = con.cursor()

    cursor.execute(
        """SELECT DISTINCT TeaterStykke.Tittel, Skuespiller.Navn, Rolle.Navn
                   FROM Skuespiller 
                   JOIN SpillesAv 
                   ON Skuespiller.SkuespillerID = SpillesAv.Skuespiller 
                   JOIN RolleIAkt ON RolleIAkt.Rolle = SpillesAv.Rolle
                   JOIN TeaterStykke ON TeaterStykke.TeaterStykkeID = RolleIAkt.TeaterStykke
                   JOIN Rolle ON RolleIAkt.Rolle = Rolle.RolleID"""
    )
    a = cursor.fetchall()
    for entry in a:
        print("\n")
        for x in entry:
            print(x)


useCase5()

# finne navn på skuespillere som opptrer i forskjellige teaterstykker.
# skriv ut navn på teaterstykke, navn på skuespiller og rolle
