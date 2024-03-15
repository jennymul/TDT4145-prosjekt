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

    #Teaterstykker
    cursor.execute('INSERT INTO Teaterstykke VALUES (1, "Kongsemnene", "Henrik Ibsen", 1)')
    cursor.execute('INSERT INTO Teaterstykke VALUES (2, "Størst av alt er Kjærligheten", "Jonas Corell Petersen", 2)')

    #Akt
    cursor.execute('INSERT INTO Akt VALUES (1, 1)')
    cursor.execute('INSERT INTO Akt VALUES (1, 2)')
    cursor.execute('INSERT INTO Akt VALUES (1, 3)')
    cursor.execute('INSERT INTO Akt VALUES (1, 4)')
    cursor.execute('INSERT INTO Akt VALUES (1, 5)')
    cursor.execute('INSERT INTO Akt VALUES (2, 1)')

    #Actors in Kongsemnene
    cursor.execute('INSERT INTO Skuespiller VALUES (1, "Arturo Scotti")')
    cursor.execute('INSERT INTO Skuespiller VALUES (2, "Ingunn Beate Strige Øyen")')
    cursor.execute('INSERT INTO Skuespiller VALUES (3, "Hans Petter Nilsen")')
    cursor.execute('INSERT INTO Skuespiller VALUES (4, "Madeleine Brandtzæg Nilsen")')
    cursor.execute('INSERT INTO Skuespiller VALUES (5, "Synnøve Fossum Eriksen")')
    cursor.execute('INSERT INTO Skuespiller VALUES (6, "Emma Caroline Deichmann")')
    cursor.execute('INSERT INTO Skuespiller VALUES (7, "Thomas Jensen Takyi"")')
    cursor.execute('INSERT INTO Skuespiller VALUES (8, "Per Bogstad Gulliksen")')
    cursor.execute('INSERT INTO Skuespiller VALUES (9, "Isak Holmen Sørensen")')
    cursor.execute('INSERT INTO Skuespiller VALUES (10, "Fabian Heidelberg Lunde")')
    cursor.execute('INSERT INTO Skuespiller VALUES (11, "Emil Olafsson")')
    cursor.execute('INSERT INTO Skuespiller VALUES (12, "Snorre Ryen Tøndel")')

    #Actors in Størst av alt er Kjærligheten
    cursor.execute('INSERT INTO Skuespiller VALUES (13, "Sunniva Du Mond Nordal")')
    cursor.execute('INSERT INTO Skuespiller VALUES (14, "Jo Saberniak")')
    cursor.execute('INSERT INTO Skuespiller VALUES (15, "Marte M. Steinholt")')
    cursor.execute('INSERT INTO Skuespiller VALUES (16, "Tor Ivar Hagen")')
    cursor.execute('INSERT INTO Skuespiller VALUES (17, "Trond-Ove Skrødal")')
    cursor.execute('INSERT INTO Skuespiller VALUES (18, "Natlie Grøndahl Tangen")')
    cursor.execute('INSERT INTO Skuespiller VALUES (19, "Åsmund Flaten")')

    #Roles in Kongsemnene
    cursor.execute('INSERT INTO Rolle VALUES (1,"Haakon Haakonssønn")')
    cursor.execute('INSERT INTO Rolle VALUES (2,"Inga fra Vartejg (Haakons mor)")')
    cursor.execute('INSERT INTO Rolle VALUES (3,"Skule jarl")')
    cursor.execute('INSERT INTO Rolle VALUES (4,"Fru Ragnhild (Skules hustru)")')
    cursor.execute('INSERT INTO Rolle VALUES (5,"Margrete (Skules datter)")')
    cursor.execute('INSERT INTO Rolle VALUES (6,"Sigrid (Skules søster) / Ingebjørg")')
    cursor.execute('INSERT INTO Rolle VALUES (7,"Biskop Nikolas")')
    cursor.execute('INSERT INTO Rolle VALUES (8,"Gregorius Jonssønn")')
    cursor.execute('INSERT INTO Rolle VALUES (9,"Paal Flida")')
    cursor.execute('INSERT INTO Rolle VALUES (10,"Trønder")')
    cursor.execute('INSERT INTO Rolle VALUES (11,"Baard Bratte")')
    cursor.execute('INSERT INTO Rolle VALUES (12,"Jatgeir Skald")')
    cursor.execute('INSERT INTO Rolle VALUES (13,"Dagfinn Bonde")')
    cursor.execute('INSERT INTO Rolle VALUES (14,"Peter(prest og Ingebjørgs sønn)")')

    #Roles in Størst av alt er Kjærligheten
    cursor.execute('INSERT INTO Rolle VALUES (15,"Sunniva Du Mond Nordal")')
    cursor.execute('INSERT INTO Rolle VALUES (16,"Jo Saberniak")')
    cursor.execute('INSERT INTO Rolle VALUES (17,"Marte M. Steinholt")')
    cursor.execute('INSERT INTO Rolle VALUES (18,"Tor Ivar Hagen")')
    cursor.execute('INSERT INTO Rolle VALUES (19,"Trond-Ove Skrødal")')
    cursor.execute('INSERT INTO Rolle VALUES (20,"Natlie Grøndahl Tangen")')
    cursor.execute('INSERT INTO Rolle VALUES (21,"Åsmund Flaten")')

    #Spilles av
    cursor.execute('INSERT INTO SpillesAv VALUES (1,1)')
    cursor.execute('INSERT INTO SpillesAv VALUES (2,2)')
    cursor.execute('INSERT INTO SpillesAv VALUES (3,3)')
    cursor.execute('INSERT INTO SpillesAv VALUES (4,4)')
    cursor.execute('INSERT INTO SpillesAv VALUES (5,5)')
    cursor.execute('INSERT INTO SpillesAv VALUES (6,6)')
    cursor.execute('INSERT INTO SpillesAv VALUES (7,7)')
    cursor.execute('INSERT INTO SpillesAv VALUES (8,8)')
    cursor.execute('INSERT INTO SpillesAv VALUES (9,9)')
    cursor.execute('INSERT INTO SpillesAv VALUES (9,10)')
    cursor.execute('INSERT INTO SpillesAv VALUES (2,2)')
    cursor.execute('INSERT INTO SpillesAv VALUES (10,10)')
    cursor.execute('INSERT INTO SpillesAv VALUES (10,11)')
    cursor.execute('INSERT INTO SpillesAv VALUES (11,12)')
    cursor.execute('INSERT INTO SpillesAv VALUES (11,13)')
    cursor.execute('INSERT INTO SpillesAv VALUES (12,14)')
    cursor.execute('INSERT INTO SpillesAv VALUES (13,15)')
    cursor.execute('INSERT INTO SpillesAv VALUES (14,16)')
    cursor.execute('INSERT INTO SpillesAv VALUES (15,17)')
    cursor.execute('INSERT INTO SpillesAv VALUES (16,18)')
    cursor.execute('INSERT INTO SpillesAv VALUES (17,19)')
    cursor.execute('INSERT INTO SpillesAv VALUES (18,20)')
    cursor.execute('INSERT INTO SpillesAv VALUES (19,21)')

    #Forestillinger Kongsemnene
    cursor.execute('INSERT INTO Forestilling VALUES ("01-02-2024", "19:00:00",1)')
    cursor.execute('INSERT INTO Forestilling VALUES ("02-02-2024", "19:00:00",1)')
    cursor.execute('INSERT INTO Forestilling VALUES ("03-02-2024", "19:00:00",1)')
    cursor.execute('INSERT INTO Forestilling VALUES ("05-02-2024", "19:00:00",1)')
    cursor.execute('INSERT INTO Forestilling VALUES ("06-02-2024", "19:00:00",1)')

    #Forestillinger Størst av alt er Kjærligheten
    cursor.execute('INSERT INTO Forestilling VALUES ("03-02-2024", "18:30:00",2)')
    cursor.execute('INSERT INTO Forestilling VALUES ("06-02-2024", "18:30:00",2)')
    cursor.execute('INSERT INTO Forestilling VALUES ("07-02-2024", "18:30:00",2)')
    cursor.execute('INSERT INTO Forestilling VALUES ("12-02-2024", "18:30:00",2)')
    cursor.execute('INSERT INTO Forestilling VALUES ("13-02-2024", "18:30:00",2)')
    cursor.execute('INSERT INTO Forestilling VALUES ("14-02-2024", "18:30:00",2)')

    #Pristype Kongsemnene
    cursor.execute('INSERT INTO PrisType VALUES ("Ordinær", 350, 1)')
    cursor.execute('INSERT INTO PrisType VALUES ("Honnør", 380, 1)')
    cursor.execute('INSERT INTO PrisType VALUES ("Student", 280, 1)')
    cursor.execute('INSERT INTO PrisType VALUES ("Gruppe 10", 420, 1)')
    cursor.execute('INSERT INTO PrisType VALUES ("Gruppe honnør", 360, 1)')

    #Pristype Størst av alt er kjærligheten
    cursor.execute('INSERT INTO PrisType VALUES ("Ordinær", 350, 2)')
    cursor.execute('INSERT INTO PrisType VALUES ("Honnør", 300, 2)')
    cursor.execute('INSERT INTO PrisType VALUES ("Student", 220, 2)')
    cursor.execute('INSERT INTO PrisType VALUES ("Barn", 220, 2)')
    cursor.execute('INSERT INTO PrisType VALUES ("Gruppe 10", 330, 2)')
    cursor.execute('INSERT INTO PrisType VALUES ("Gruppe honnør 10", 270, 2)')

    #Roller i Akt
    cursor.execute('INSERT INTO RolleIAkt VALUES (1,1,1)')
    cursor.execute('INSERT INTO RolleIAkt VALUES (1,2,1)')
    cursor.execute('INSERT INTO RolleIAkt VALUES (1,3,1)')
    cursor.execute('INSERT INTO RolleIAkt VALUES (1,4,1)')
    cursor.execute('INSERT INTO RolleIAkt VALUES (1,5,1)')
    cursor.execute('INSERT INTO RolleIAkt VALUES (13,1,1)')
    cursor.execute('INSERT INTO RolleIAkt VALUES (13,2,1)')
    cursor.execute('INSERT INTO RolleIAkt VALUES (13,3,1)')
    cursor.execute('INSERT INTO RolleIAkt VALUES (13,4,1)')
    cursor.execute('INSERT INTO RolleIAkt VALUES (13,5,1)')
    cursor.execute('INSERT INTO RolleIAkt VALUES (12,4,1)')
    cursor.execute('INSERT INTO RolleIAkt VALUES (6,1,1)')
    cursor.execute('INSERT INTO RolleIAkt VALUES (6,2,1)')
    cursor.execute('INSERT INTO RolleIAkt VALUES (6,5,1)')
    cursor.execute('INSERT INTO RolleIAkt VALUES (3,1,1)')
    cursor.execute('INSERT INTO RolleIAkt VALUES (3,2,1)')
    cursor.execute('INSERT INTO RolleIAkt VALUES (3,3,1)')
    cursor.execute('INSERT INTO RolleIAkt VALUES (3,4,1)')
    cursor.execute('INSERT INTO RolleIAkt VALUES (3,5,1)')
    cursor.execute('INSERT INTO RolleIAkt VALUES (4,1,1)')
    cursor.execute('INSERT INTO RolleIAkt VALUES (4,5,1)')
    cursor.execute('INSERT INTO RolleIAkt VALUES (8,1,1)')
    cursor.execute('INSERT INTO RolleIAkt VALUES (8,2,1)')
    cursor.execute('INSERT INTO RolleIAkt VALUES (8,3,1)')
    cursor.execute('INSERT INTO RolleIAkt VALUES (8,4,1)')
    cursor.execute('INSERT INTO RolleIAkt VALUES (8,5,1)')
    cursor.execute('INSERT INTO RolleIAkt VALUES (5,1,1)')
    cursor.execute('INSERT INTO RolleIAkt VALUES (5,2,1)')
    cursor.execute('INSERT INTO RolleIAkt VALUES (5,3,1)')
    cursor.execute('INSERT INTO RolleIAkt VALUES (5,4,1)')
    cursor.execute('INSERT INTO RolleIAkt VALUES (5,5,1)')
    cursor.execute('INSERT INTO RolleIAkt VALUES (7,1,1)')
    cursor.execute('INSERT INTO RolleIAkt VALUES (7,2,1)')
    cursor.execute('INSERT INTO RolleIAkt VALUES (7,3,1)')
    cursor.execute('INSERT INTO RolleIAkt VALUES (14,3,1)')
    cursor.execute('INSERT INTO RolleIAkt VALUES (14,4,1)')
    cursor.execute('INSERT INTO RolleIAkt VALUES (14,5,1)')
    
    cursor.execute('INSERT INTO RolleIAkt VALUES(15,1,2)')
    cursor.execute('INSERT INTO RolleIAkt VALUES(16,1,2)')
    cursor.execute('INSERT INTO RolleIAkt VALUES(17,1,2)')
    cursor.execute('INSERT INTO RolleIAkt VALUES(18,1,2)')
    cursor.execute('INSERT INTO RolleIAkt VALUES(19,1,2)')
    cursor.execute('INSERT INTO RolleIAkt VALUES(20,1,2)')
    cursor.execute('INSERT INTO RolleIAkt VALUES(21,1,2)')

    #Ansatte
    cursor.execute('INSERT INTO Ansatt VALUES (1,"Yury Butusov","Fast","yurybutusov@trondelagteater.no")')
    cursor.execute('INSERT INTO Ansatt VALUES (2, "Aleksandr Shishkin-Hokusai", "Fast", aleksandrshishkin-hokusai@trondelagteater.no")')
    cursor.execute('INSERT INTO Ansatt VALUES (3, "Eivind Myren", "Fast", "eivindmyren@trondelagteater.no")')
    cursor.execute('INSERT INTO Ansatt VALUES (4, "Mina Rype Stokke", "Fast", "minarypestokke@trondelagteater.no")')
    cursor.execute('INSERT INTO Ansatt VALUES (5, "Jonas Corell Petersen", "Fast", "jonaspetersen@trondelagteater.no")')
    cursor.execute('INSERT INTO Ansatt VALUES (6, "David Gehrt", "Fast", "davidghert@trondelagteater.no")')
    cursor.execute('INSERT INTO Ansatt VALUES(7, "Gaute Tønder", "Fast", "gautetonder@trondelagteater.no")')
    cursor.execute('INSERT INTO Ansatt VALUES(8, "Magnus Mikaelsen", "Fast", "magnusmikaelsen@trondelagteater.no")')
    cursor.execute('INSERT INTO Ansatt VALUES(9, "Kristoffer Spender", "Fast", "kristofferspender@trondelagteater.no")')
    
    #Oppgaver
    cursor.execute('INSERT INTO Oppgave VALUES (1,"Regi","regissør",2)')
    cursor.execute('INSERT INTO Oppgave VALUES (2,"Scenografi","Fikse scene",2)')
    cursor.execute('INSERT INTO Oppgave VALUES (3,"Kostyme","Fikse kostymer",2)')
    cursor.execute('INSERT INTO Oppgave VALUES (4,"Musikalsk ansvarlig","Ansvar for musikk",2)')
    cursor.execute('INSERT INTO Oppgave VALUES (5,"Lysdesign","Fikse lys",2)')
    cursor.execute('INSERT INTO Oppgave VALUES (6,"Dramaturg","Fikse drama",2)')

    cursor.execute('INSERT INTO Oppgave VALUES (7,"Regi","regissør",1)')
    cursor.execute('INSERT INTO Oppgave VALUES (8,"Musikkutvelgelse","Velge ut musikk",1)')
    cursor.execute('INSERT INTO Oppgave VALUES (9,"Scenografi","Fikse scene",1)')
    cursor.execute('INSERT INTO Oppgave VALUES (10,"Kostyme","Fikse kostymer",1)')
    cursor.execute('INSERT INTO Oppgave VALUES (11,"Lysdesign","Fikse lys",1)')
    cursor.execute('INSERT INTO Oppgave VALUES (12,"Dramaturg","Fikse drama",1)')



    #TildeltOppgave
    cursor.execute('INSERT INTO TildeltOppgave VALUES (5,1)')
    cursor.execute('INSERT INTO TildeltOppgave VALUES (6,2)')
    cursor.execute('INSERT INTO TildeltOppgave VALUES (6,3)')
    cursor.execute('INSERT INTO TildeltOppgave VALUES (7,4)')
    cursor.execute('INSERT INTO TildeltOppgave VALUES (8,5)')
    cursor.execute('INSERT INTO TildeltOppgave VALUES (9,6)')

    cursor.execute('INSERT INTO TildeltOppgave VALUES (10,7)')
    cursor.execute('INSERT INTO TildeltOppgave VALUES (10,8)')
    cursor.execute('INSERT INTO TildeltOppgave VALUES (11,9)')
    cursor.execute('INSERT INTO TildeltOppgave VALUES (11,10)')
    cursor.execute('INSERT INTO TildeltOppgave VALUES (12,11)')
    cursor.execute('INSERT INTO TildeltOppgave VALUES (13,12)')


    con.commit()

fillDatabase()