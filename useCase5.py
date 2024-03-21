import sqlite3
from utils import printTable

def printAllActorsInShows():
    con = sqlite3.connect("trondelagTeater.db")
    cursor = con.cursor()

    cursor.execute("""
    SELECT DISTINCT TeaterStykke.Tittel, Skuespiller.Navn, Rolle.Navn
    FROM Skuespiller 
    JOIN SpillesAv ON Skuespiller.SkuespillerID = SpillesAv.Skuespiller 
    JOIN RolleIAkt ON RolleIAkt.Rolle = SpillesAv.Rolle
    JOIN TeaterStykke ON TeaterStykke.TeaterStykkeID = RolleIAkt.TeaterStykke
    JOIN Rolle ON RolleIAkt.Rolle = Rolle.RolleID"""
    )
    result = cursor.fetchall()

    printTable(['TeaterStykke', 'Skuespiller', 'Rolle'], result)
    con.close()

printAllActorsInShows()
