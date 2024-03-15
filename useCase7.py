import sqlite3

def useCase7(actorName):
    con = sqlite3.connect("trondelagTeater.db")
    cursor = con.cursor()
    cursor.execute("""SELECT DISTINCT Skuespiller.Navn 
                    FROM RolleIAkt
                    JOIN SpillesAv ON SpillesAv.Rolle = RolleIAkt.Rolle
                    JOIN Skuespiller ON Skuespiller.SkuespillerID = SpillesAv.Skuespiller
                    JOIN (
                        SELECT Akt, TeaterStykke 
                        FROM Skuespiller
                        JOIN SpillesAv ON Skuespiller.SkuespillerID = SpillesAv.Skuespiller
                        JOIN RolleIAkt ON RolleIAkt.Rolle = SpillesAv.Rolle
                        WHERE Skuespiller.Navn = ?
                    ) AS SkuespillerInfo ON RolleIAkt.Akt = SkuespillerInfo.Akt AND RolleIAkt.TeaterStykke = SkuespillerInfo.TeaterStykke;
                    """,[actorName])
    print(cursor.fetchall())


