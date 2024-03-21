import sqlite3
from utils import printTable


def printActorsPlayedInSameActAsActor(actor_name):
    con = sqlite3.connect("trondelagTeater.db")
    cursor = con.cursor()

    cursor.execute(
        """
    SELECT DISTINCT Skuespiller.Navn, TeaterStykke.Tittel
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
    """,
        [actor_name],
    )

    result = cursor.fetchall()
    result = [(actor_name, row[0], row[1]) for row in result]
    printTable(
        ["Skuespiller A", "Skuespiller B", "TeaterStykke"], result
    )  # TODO Ikke printe når Skuespiller A = Skuespiller B


actor_name = input("Skriv inn skuespillernavn: ")
printActorsPlayedInSameActAsActor(actor_name)
