import os
import sqlite3
import math

def fillDatabase():
    con = sqlite3.connect("trondelagTeater.db")
    cursor = con.cursor()
    cursor.execute("""PRAGMA encoding = "UTF-8" """)

    cursor.execute('INSERT INTO TeaterSal VALUES (1, "Hovedscenen", 524)')
    cursor.execute('INSERT INTO TeaterSal VALUES (2, "Gamle Scene", 320)')
    #We want to insert the rows 1-16 in main scene as these are just straight forward double loop
    for seat in range(1,449):
        cursor.execute("INSERT INTO Plass (StolNummer, RadNummer, Omraade, Sal) VALUES (?, ?, 'Parkett', '1');", [seat, math.ceil(seat/28)])

    #The next 2 rows have "holes" in 4 seats from 
    for seat in range(449,505):
        if (seat in range(467, 471)) or (seat in range(495, 499)):
            continue
        cursor.execute("INSERT INTO Plass (StolNummer, RadNummer, Omraade, Sal) VALUES (?, ?, 'Parkett', '1');", [seat, math.ceil(seat/28)])

    #Now we want to do both galleries
    for seat in range(505,510):
        cursor.execute("INSERT INTO Plass (StolNummer, RadNummer, Omraade, Sal) VALUES (?, 1, 'Venstre Galleri', '1');", [seat])
    for seat in range(515,520):
        cursor.execute("INSERT INTO Plass (StolNummer, RadNummer, Omraade, Sal) VALUES (?, 0, 'Venstre Galleri', '1');", [seat])

    for seat in range(510,515):
        cursor.execute("INSERT INTO Plass (StolNummer, RadNummer, Omraade, Sal) VALUES (?, 0, 'Høyre Galleri', '1');", [seat])
    for seat in range(520,525):
        cursor.execute("INSERT INTO Plass (StolNummer, RadNummer, Omraade, Sal) VALUES (?, 1, 'Høyre Galleri', '1');", [seat])


    #For the old scene we need a mapping between amount of seats to rows due to inconsistencies.
    #Main floor:
    main_row_seat_mapping = [
        (1,18),
        (2,16),
        (3,17),
        (4,18),
        (5,18),
        (6,17),
        (7,18),
        (8,17),
        (9,17),
        (10, 14)
    ]

    for mapping in main_row_seat_mapping:
        for seat in range(1, mapping[1]+1):
            cursor.execute("INSERT INTO Plass (StolNummer, RadNummer, Omraade, Sal) VALUES (?, ?, 'Parkett', '2');", [seat, mapping[0]])

    #Now similarly for balcony:
    balcony_row_seat_mapping = [
        (1,28),
        (2,27),
        (3,22),
        (4,17),
    ]
    for mapping in balcony_row_seat_mapping:
        for seat in range(1, mapping[1]+1):
            cursor.execute("INSERT INTO Plass (StolNummer, RadNummer, Omraade, Sal) VALUES (?, ?, 'Balkong', '2');", [seat, mapping[0]])

    #And gallery

    gallery_row_seat_mapping = [
        (1,33),
        (2,18),
        (3,17),
    ]
    for mapping in gallery_row_seat_mapping:
        for seat in range(1, mapping[1]+1):
            cursor.execute("INSERT INTO Plass (StolNummer, RadNummer, Omraade, Sal) VALUES (?, ?, 'Galleri', '2');", [seat, mapping[0]])



    con.commit()

fillDatabase()