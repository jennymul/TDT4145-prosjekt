import sqlite3
from utils import getTicketPrice, getNextPrimaryKey

# Values given in the task description
show_date = "03-02-2024"
show_time = "18:30:00"
ticket_price_type = "Ordinær"
ticket_count = 9
customer_id = 1

play_id = 2  # TODO
hall_id = 2  # TODO

con = sqlite3.connect("trondelagTeater.db")
cursor = con.cursor()

cursor.execute(
    """
SELECT P.RadNummer, P.StolNummer, P.Omraade
FROM Plass AS P
WHERE P.Sal = ?
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
""",
    [hall_id],
)
available_seats = cursor.fetchall()


def findSeatsOnSameRow(seats, seat_count):
    for i in range(len(seats)):
        row_number = seats[i][0]
        seats_on_same_row = [seats[i]]

        for j in range(i + 1, len(seats)):
            if len(seats_on_same_row) == seat_count or seats[j][0] != row_number:
                break

            seats_on_same_row.append(seats[j])

        if len(seats_on_same_row) == seat_count:
            return seats_on_same_row

    return []


seats_to_buy = findSeatsOnSameRow(available_seats, ticket_count)

ticket_price = getTicketPrice(cursor, ticket_price_type)
total_ticket_price = ticket_price * ticket_count

ticket_purchase_id = getNextPrimaryKey(cursor, "KjopID", "BillettKjop")
cursor.execute(
    """
INSERT INTO BillettKjop VALUES (?, ?, ?, ?, ?);
""",
    (ticket_purchase_id, total_ticket_price, show_date, show_time, customer_id),
)

ticket_id = getNextPrimaryKey(cursor, "BillettID", "Billett")
for seat in seats_to_buy:
    row_number = seat[0]
    seat_number = seat[1]
    hall_area_name = seat[2]

    cursor.execute(
        """
    INSERT INTO Billett VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """,
        (
            ticket_id,
            ticket_price_type,
            seat_number,
            row_number,
            hall_area_name,
            show_date,
            show_time,
            hall_id,
            play_id,
            ticket_purchase_id,
        ),
    )
    ticket_id += 1

    print(
        f"Kjøpte en {ticket_price_type} billett på setenummer {seat_number} og radnummer {row_number} i salområdet {hall_area_name}"
    )

con.commit()
con.close()
