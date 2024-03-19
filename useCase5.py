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

    print("Kongsemnene:")
    for x in a:
        if(x[0] == "Kongsemnene"):
            print(f'Skuespiller: {x[1]} - Rolle: {x[2]}')
    print("\nStørst av alt er Kjærligheten:")
    for x in a:
        if(x[0] == "Størst av alt er Kjærligheten"):
            print(f'Skuespiller: {x[1]} - Rolle: {x[2]}')

useCase5()

