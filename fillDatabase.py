from datetime import datetime
import os
import re
import sqlite3
import math
import asyncio


def insertHovedscenen(cursor):
    cursor.execute("""INSERT INTO TeaterSal VALUES (1, 'Hovedscenen', 524)""")

    # We want to insert the rows 1-16 in main scene as these are just straight forward double loop
    for seat in range(1, 449):
        cursor.execute(
            "INSERT INTO Plass (StolNummer, RadNummer, Omraade, Sal) VALUES (?, ?, 'Parkett', '1');",
            [seat, math.ceil(seat / 28)],
        )

    # The next 2 rows have "holes" in 4 seats from
    for seat in range(449, 505):
        if (seat in range(467, 471)) or (seat in range(495, 499)):
            continue
        cursor.execute(
            "INSERT INTO Plass (StolNummer, RadNummer, Omraade, Sal) VALUES (?, ?, 'Parkett', '1');",
            [seat, math.ceil(seat / 28)],
        )

    # Now we want to do both galleries
    for seat in range(505, 510):
        cursor.execute(
            "INSERT INTO Plass (StolNummer, RadNummer, Omraade, Sal) VALUES (?, 1, 'Galleri', '1');",
            [seat],
        )
    for seat in range(515, 520):
        cursor.execute(
            "INSERT INTO Plass (StolNummer, RadNummer, Omraade, Sal) VALUES (?, 2, 'Galleri', '1');",
            [seat],
        )

    for seat in range(510, 515):
        cursor.execute(
            "INSERT INTO Plass (StolNummer, RadNummer, Omraade, Sal) VALUES (?, 3, 'Galleri', '1');",
            [seat],
        )
    for seat in range(520, 525):
        cursor.execute(
            "INSERT INTO Plass (StolNummer, RadNummer, Omraade, Sal) VALUES (?, 4, 'Galleri', '1');",
            [seat],
        )


def insertGamleScene(cursor):
    cursor.execute("""INSERT INTO TeaterSal VALUES (2, "Gamle Scene", 320)""")
    # Main floor:
    main_row_seat_mapping = [
        (1, 18),
        (2, 16),
        (3, 17),
        (4, 18),
        (5, 18),
        (6, 17),
        (7, 18),
        (8, 17),
        (9, 17),
        (10, 14),
    ]

    for mapping in main_row_seat_mapping:
        for seat in range(1, mapping[1] + 1):
            cursor.execute(
                "INSERT INTO Plass (StolNummer, RadNummer, Omraade, Sal) VALUES (?, ?, 'Parkett', '2');",
                [seat, mapping[0]],
            )

    # Now similarly for balcony:
    balcony_row_seat_mapping = [
        (1, 28),
        (2, 27),
        (3, 22),
        (4, 17),
    ]
    for mapping in balcony_row_seat_mapping:
        for seat in range(1, mapping[1] + 1):
            cursor.execute(
                "INSERT INTO Plass (StolNummer, RadNummer, Omraade, Sal) VALUES (?, ?, 'Balkong', '2');",
                [seat, mapping[0]],
            )

    # And gallery

    gallery_row_seat_mapping = [
        (1, 33),
        (2, 18),
        (3, 17),
    ]
    for mapping in gallery_row_seat_mapping:
        for seat in range(1, mapping[1] + 1):
            cursor.execute(
                "INSERT INTO Plass (StolNummer, RadNummer, Omraade, Sal) VALUES (?, ?, 'Galleri', '2');",
                [seat, mapping[0]],
            )


ticket_id = 1


def insertTicketsFromFile(cursor, filename, hall_id, play_id, show_time):
    global ticket_id
    ticket_price = 350  # We assume that only ordinary tickets are purchased

    dummy_current_date = "01-02-2024"
    dummy_current_time = "10:00:00"

    date = None

    floors = []
    current_floor = None

    with open(filename, "r") as file:
        date_components = file.readline().strip()[5:].split("-")
        date = date_components[2] + "-" + date_components[1] + "-" + date_components[0]

        for line in file:
            line = line.strip()
            if line.isalpha():
                if current_floor:
                    floors.append(current_floor)
                current_floor = (line, [])
            elif current_floor is not None:
                current_floor[1].append(line)

        if current_floor:
            floors.append(current_floor)

    for floor in floors:
        floor_name = floor[0]

        for row_number, row in enumerate(reversed(floor[1])):
            for seat_number, seat in enumerate(row):
                if seat != "1":
                    continue

                cursor.execute(
                    'INSERT INTO BillettKjop VALUES(?, ?, ?, ?, "1" )',
                    [ticket_id, ticket_price, dummy_current_date, dummy_current_time],
                )

                cursor.execute(
                    "INSERT INTO Billett VALUES(?, 'Ordinær', ?, ?, ?, ?, ?, ?, ?, ?)",
                    [
                        ticket_id,
                        seat_number + 1,
                        row_number + 1,
                        floor_name,
                        date,
                        show_time,
                        hall_id,
                        play_id,
                        ticket_id,
                    ],
                )

                ticket_id += 1


async def fillDatabase():
    con = sqlite3.connect("trondelagTeater.db")
    cursor = con.cursor()
    cursor.execute('PRAGMA encoding = "UTF-8"')

    insertHovedscenen(cursor)
    insertGamleScene(cursor)

    # Teaterstykker
    cursor.execute(
        """INSERT INTO TeaterStykke VALUES
            (1, "Kongsemnene", "Henrik Ibsen", 1),
            (2, "Størst av alt er Kjærligheten", "Jonas Corell Petersen", 2);
    """
    )

    # Akt
    cursor.execute(
        """INSERT INTO Akt VALUES
        (1, 1),
        (1, 2),
        (1, 3),
        (1, 4),
        (1, 5),
        (2, 1);"""
    )

    # Actors in Kongsemnene
    cursor.execute(
        """INSERT INTO Skuespiller VALUES
        (1, "Arturo Scotti"),
        (2, "Ingunn Beate Strige Øyen"),
        (3, "Hans Petter Nilsen"),
        (4, "Madeleine Brandtzæg Nilsen"),
        (5, "Synnøve Fossum Eriksen"),
        (6, "Emma Caroline Deichmann"),
        (7, "Thomas Jensen Takyi"),
        (8, "Per Bogstad Gulliksen"),
        (9, "Isak Holmen Sørensen"),
        (10, "Fabian Heidelberg Lunde"),
        (11, "Emil Olafsson"),
        (12, "Snorre Ryen Tøndel");
    """
    )

    # Actors in Størst av alt er Kjærligheten
    cursor.execute(
        """INSERT INTO Skuespiller VALUES
        (13, "Sunniva Du Mond Nordal"),
        (14, "Jo Saberniak"),
        (15, "Marte M. Steinholt"),
        (16, "Tor Ivar Hagen"),
        (17, "Trond-Ove Skrødal"),
        (18, "Natlie Grøndahl Tangen"),
        (19, "Åsmund Flaten");
    """
    )

    # Roles in Kongsemnene
    cursor.execute(
        """INSERT INTO Rolle VALUES
        (1,"Haakon Haakonssønn"),
        (2,"Inga fra Vartejg (Haakons mor)"),
        (3,"Skule jarl"),
        (4,"Fru Ragnhild (Skules hustru)"),
        (5,"Margrete (Skules datter)"),
        (6,"Sigrid (Skules søster) / Ingebjørg"),
        (7,"Biskop Nikolas"),
        (8,"Gregorius Jonssønn"),
        (9,"Paal Flida"),
        (10,"Trønder"),
        (11,"Baard Bratte"),
        (12,"Jatgeir Skald"),
        (13,"Dagfinn Bonde"),
        (14,"Peter(prest og Ingebjørgs sønn)");
    """
    )

    # Roles in Størst av alt er Kjærligheten
    cursor.execute(
        """INSERT INTO Rolle VALUES
        (15,"Sunniva Du Mond Nordal"),
        (16,"Jo Saberniak"),
        (17,"Marte M. Steinholt"),
        (18,"Tor Ivar Hagen"),
        (19,"Trond-Ove Skrødal"),
        (20,"Natlie Grøndahl Tangen"),
        (21,"Åsmund Flaten");
    """
    )

    # Spilles av
    cursor.execute(
        """INSERT INTO SpillesAv VALUES
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
        (6,6),
        (7,7),
        (8,8),
        (9,9),
        (9,10),
        (10,10),
        (10,11),
        (11,12),
        (11,13),
        (12,14),
        (13,15),
        (14,16),
        (15,17),
        (16,18),
        (17,19),
        (18,20),
        (19,21);
    """
    )

    # Forestillinger Kongsemnene
    cursor.execute(
        """INSERT INTO Forestilling VALUES
        ("01-02-2024", "19:00:00",1),
        ("02-02-2024", "19:00:00",1),
        ("03-02-2024", "19:00:00",1),
        ("05-02-2024", "19:00:00",1),
        ("06-02-2024", "19:00:00",1);
    """
    )

    # Forestillinger Størst av alt er Kjærligheten
    cursor.execute(
        """INSERT INTO Forestilling VALUES
        ("03-02-2024", "18:30:00", 2),
        ("06-02-2024", "18:30:00", 2),
        ("07-02-2024", "18:30:00", 2),
        ("12-02-2024", "18:30:00", 2),
        ("13-02-2024", "18:30:00", 2),
        ("14-02-2024", "18:30:00", 2);
    """
    )

    # Pristype Kongsemnene
    cursor.execute(
        """INSERT INTO PrisType VALUES
        ("Ordinær", 350, 1),
        ("Honnør", 380, 1),
        ("Student", 280, 1),
        ("Gruppe 10", 420, 1),
        ("Gruppe honnør", 360, 1);
    """
    )

    # Pristype Størst av alt er kjærligheten
    cursor.execute(
        """INSERT INTO PrisType VALUES
        ("Ordinær", 350, 2),
        ("Honnør", 300, 2),
        ("Student", 220, 2),
        ("Barn", 220, 2),
        ("Gruppe 10", 330, 2),
        ("Gruppe honnør 10", 270, 2);
    """
    )

    # Roller i Akt
    cursor.execute(
        """INSERT INTO RolleIAkt VALUES
        (1,1,1),
        (1,2,1),
        (1,3,1),
        (1,4,1),
        (1,5,1),
        (13,1,1),
        (13,2,1),
        (13,3,1),
        (13,4,1),
        (13,5,1),
        (12,4,1),
        (6,1,1),
        (6,2,1),
        (6,5,1),
        (3,1,1),
        (3,2,1),
        (3,3,1),
        (3,4,1),
        (3,5,1),
        (4,1,1),
        (4,5,1),
        (9,1,1),
        (9,2,1),
        (9,3,1),
        (9,4,1),
        (9,5,1),
        (8,1,1),
        (8,2,1),
        (8,3,1),
        (8,4,1),
        (8,5,1),
        (5,1,1),
        (5,2,1),
        (5,3,1),
        (5,4,1),
        (5,5,1),
        (7,1,1),
        (7,2,1),
        (7,3,1),
        (14,3,1),
        (14,4,1),
        (14,5,1);
    """
    )

    cursor.execute(
        """INSERT INTO RolleIAkt VALUES
        (15,1,2),
        (16,1,2),
        (17,1,2),
        (18,1,2),
        (19,1,2),
        (20,1,2),
        (21,1,2);
    """
    )

    # Ansatte
    cursor.execute(
        """INSERT INTO Ansatt VALUES
        (1,"Yury Butusov","Fast","yurybutusov@trondelagteater.no"),
        (2, "Aleksandr Shishkin-Hokusai", "Fast", "aleksandrshishkin-hokusai@trondelagteater.no"),
        (3, "Eivind Myren", "Fast", "eivindmyren@trondelagteater.no"),
        (4, "Mina Rype Stokke", "Fast", "minarypestokke@trondelagteater.no"),
        (5, "Jonas Corell Petersen", "Fast", "jonaspetersen@trondelagteater.no"),
        (6, "David Gehrt", "Fast", "davidghert@trondelagteater.no"),
        (7, "Gaute Tønder", "Fast", "gautetonder@trondelagteater.no"),
        (8, "Magnus Mikaelsen", "Fast", "magnusmikaelsen@trondelagteater.no"),
        (9, "Kristoffer Spender", "Fast", "kristofferspender@trondelagteater.no");
    """
    )

    # Bruker
    cursor.execute(
        """INSERT INTO Kunde VALUES(1,"Navn Navnesen", "Parkgata 1", "navn@gmail.com")"""
    )

    # Oppgaver
    cursor.execute(
        """INSERT INTO Oppgave VALUES
        (1, "Regi", "regissør", 2),
        (2, "Scenografi", "Fikse scene", 2),
        (3, "Kostyme", "Fikse kostymer", 2),
        (4, "Musikalsk ansvarlig", "Ansvar for musikk", 2),
        (5, "Lysdesign", "Fikse lys", 2),
        (6, "Dramaturg", "Fikse drama", 2),
        (7, "Regi", "regissør", 1),
        (8, "Musikkutvelgelse", "Velge ut musikk", 1),
        (9, "Scenografi", "Fikse scene", 1),
        (10, "Kostyme", "Fikse kostymer", 1),
        (11, "Lysdesign", "Fikse lys", 1),
        (12, "Dramaturg", "Fikse drama", 1);
    """
    )

    # TildeltOppgave
    cursor.execute(
        """INSERT INTO TildeltOppgave VALUES
        (5, 1),
        (6, 2),
        (6, 3),
        (7, 4),
        (8, 5),
        (9, 6),
        (10, 7),
        (10, 8),
        (11, 9),
        (11, 10),
        (12, 11),
        (13, 12);
    """
    )

    insertTicketsFromFile(cursor, "filesneeded/hovedscenen.txt", 1, 1, "19:00:00")
    insertTicketsFromFile(cursor, "filesneeded/gamle-scene.txt", 2, 2, "18:30:00")

    con.commit()
    con.close()
